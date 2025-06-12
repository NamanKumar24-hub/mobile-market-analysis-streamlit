-- =======================
--  Data Overview
-- =======================

-- Sample of model summary
SELECT TOP 5 * 
FROM brand_model_summary;

-- Sample of cleaned mobile data ordered by memory
SELECT TOP 5 * 
FROM cleaned_mobile_data
ORDER BY memory;

-- Sample of price segment definitions
SELECT TOP 5 * 
FROM price_segment_limits;

-- =======================
-- Initial Updates
-- =======================

-- Round values for cleaner analysis
-- UPDATE brand_model_summary 
-- SET avg_price = ROUND(avg_price, 2);

-- UPDATE cleaned_mobile_data 
-- SET 
--     rating = ROUND(rating, 1), 
--     discount_percent = ROUND(discount_percent, 2);

-- =======================
-- Assessment Queries
-- =======================

-- Q3: Which brand covers ALL 5 price segments (Entry, Budget, Mid-Range, Premium, Flagship)?
SELECT brand
FROM cleaned_mobile_data
GROUP BY brand
HAVING COUNT(DISTINCT price_segment) = 5;

-- Q4: Most common specifications offered (at least 10 variants sharing same spec)
SELECT 
    memory, 
    storage, 
    color, 
    rating, 
    COUNT(*) AS specs_count
FROM cleaned_mobile_data
GROUP BY memory, storage, color, rating
HAVING COUNT(*) >= 10
ORDER BY specs_count DESC;

-- Q5: Detailed Insights from Data

-- 1️⃣ Price Segment Coverage per Brand
SELECT 
    brand, 
    COUNT(DISTINCT price_segment) AS segments_covered
FROM cleaned_mobile_data
GROUP BY brand;

-- 2️⃣ Most Common Storage Capacities
SELECT 
    storage, 
    COUNT(*) AS occurrences
FROM cleaned_mobile_data
GROUP BY storage
ORDER BY occurrences DESC;

-- 3️⃣ Average Selling Price & Variant Count by Brand and Model
SELECT 
    brand, 
    model, 
    COUNT(*) AS num_variants, 
    ROUND(AVG(selling_price), 2) AS avg_price
FROM cleaned_mobile_data
GROUP BY brand, model
ORDER BY avg_price DESC;

-- 4️⃣ List of All Models With No Discounts
SELECT 
    brand, 
    model, 
    selling_price, 
    discount_percent
FROM cleaned_mobile_data
WHERE discount_percent = 0;

-- 5️⃣ Segment Leader: Brand with Most Variants per Segment
WITH variant_counts AS (
    SELECT 
        brand,
        price_segment,
        COUNT(DISTINCT CONCAT(model, '_', color, '_', memory, '_', storage)) AS variant_count
    FROM cleaned_mobile_data
    GROUP BY brand, price_segment
),
ranked_brands AS (
    SELECT *,
           RANK() OVER (PARTITION BY price_segment ORDER BY variant_count DESC) AS rnk
    FROM variant_counts
)
SELECT 
    brand, 
    price_segment, 
    variant_count
FROM ranked_brands
WHERE rnk = 1;
