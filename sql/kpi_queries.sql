-- Conversões totais
SELECT COUNT(*) as total_conversions
FROM dataset
WHERE Revenue = TRUE;

-- Taxa de conversão
SELECT AVG(CAST(Revenue AS FLOAT)) as conversion_rate
FROM dataset;

-- Conversão por tipo de visitante
SELECT VisitorType, AVG(CAST(Revenue AS FLOAT)) as conv_rate
FROM dataset
GROUP BY VisitorType;

-- Conversão por dia da semana
SELECT DayOfWeek, AVG(CAST(Revenue AS FLOAT)) as conv_rate
FROM dataset
GROUP BY DayOfWeek;

-- Conversão por mês
SELECT Month, AVG(CAST(Revenue AS FLOAT)) as conv_rate
FROM dataset
GROUP BY Month;