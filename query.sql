--TRANSACTIONAL QUERY
--1) Mencari mobil keluaran 2015 ke atas
select
	*
from product_detail
where year >= '2015'
order by year asc;

--2) Menambahkan satu data bid produk baru
--insert into bids
--values(201, 8, 20, 90000000,'2024-08-06 13:05:44');

select * from bids;

--3) Melihat semua mobil yang dijual 1 akun dari yang paling baru
select
	*
from product_ads pa
join product_detail pd
	using(ad_id)
where user_id ='17'
order by pa.created_at desc;

--4) mencari mobil bekas yang termurah berdasarkan keyword
select
	product_id,
	ad_id,
	model,
	year,
	price
from product_detail
where model ILIKE '%honda%'
order by 2 asc;

--5) mencari mobil bekas terdekat dengan id kota 3173
select
	product_id,
	ad_id,
	brand,
	model,
	year,
	price,
	sqrt(power((select latitude from city where city_id = '3173') - latitude, 2) + POWER((select longitude from city where city_id = '3173') - longitude, 2))as distance
from product_ads p
join product_detail using(ad_id)
join users u using(user_id)
join city c	using(city_id)
order by distance asc;

--ANALYTICAL QUERY
--1) ranking popularitas model mobil berdasarkan jumlah bid
select
    model,
    count(distinct product_id) as count_product,
    count(bid_id) as count_bid
from product_ads
left join bids
    using(ad_id)
join product_detail
    using(ad_id)
group by 1
order by 3 desc;

--2) membandingkan harga mobil berdasarkan harga rata-rata per kota
select
	city_name,
	brand,
	model,
	year,
	price,
	round(avg(price) over(partition by city_id 
						  range between unbounded preceding and unbounded following))
from product_ads
join product_detail using(ad_id)
join users using(user_id)
join city using(city_id);

--3) dari penawaran suatu model mobil,
-- cari perbandingan tanggal user melakukan bid 
-- dengan bid selanjutnya beserta harga tawar yang diberikan
with cte as(
select
	model,
	buyer_id,
	created_at as first_bid_date,
	lead(created_at, 1) over(partition by buyer_id, model order by created_at) as next_bid_date,
	price as first_bid_price,
	lead(price, 1) over(partition by buyer_id, model order by created_at) next_bid_price
from bids
join product_detail using(ad_id)
where model = 'Toyota Calya'
order by 3
)
select
	*
from cte
where next_bid_date is not null;

--4) membandingkan persentase perbedaan rata-rata harga mobil
--berdasarkan mobilnya dan rata-rata harga bid yang ditawarkan
--oleh customer pada 6 bulan terakhir
with bid_last_6mo as(
	select
		model,
		round(avg(bid_price),0) as avg_bid_6month
	from bids
	join product_detail using(ad_id) 
	where created_at >= current_date - interval '6 months'
	group by 1
),
price as(
	select
		model,
		round(avg(price),0) as avg_price
	from bids
	join product_detail using(ad_id)
	group by 1
)
select
	p.model,
	p.avg_price,
	b.avg_bid_6month,
	p.avg_price - b.avg_bid_6month as difference,
	round((p.avg_price - b.avg_bid_6month) / p.avg_price * 100, 2) as difference_percent
from bid_last_6mo b
join price p
	using(model);

--5) membuat window function rata-rata harga bid sebuah merk dan model mobil
--selama 6 bulan terakhir
with cte as(
select
	date_trunc('month', created_at) as month,
	brand,
	model,
	round(avg(price),0) as avg_price
from bids
join product_detail
	using(ad_id)
where model = 'Toyota Calya'
	and created_at >= current_date - interval '6 months'
group by 1, 2, 3
)

select
	brand,
	model,
	avg_price m_min_6,
	lag(avg_price, 1) over(order by month desc) m_min_5,
	lag(avg_price, 2) over(order by month desc) m_min_4,
	lag(avg_price, 3) over(order by month desc) m_min_3,
	lag(avg_price, 4) over(order by month desc) m_min_2,
	lag(avg_price, 5) over(order by month desc) m_min_1
from cte
order by month asc
limit 1
