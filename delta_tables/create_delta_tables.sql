CREATE TABLE transactions_delta
USING DELTA
LOCATION '/delta/transactions';

CREATE TABLE fraud_transactions
USING DELTA
AS
SELECT *
FROM transactions_delta
WHERE amount > 200;
