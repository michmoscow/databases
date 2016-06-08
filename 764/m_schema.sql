DROP TABLE IF EXISTS StockQuotes;
CREATE TABLE StockQuotes(
   company TEXT,
   week INT,
   share_price INT );
CREATE OR REPLACE FUNCTION GenerateData() RETURNS VOID AS $$
DECLARE
  _all_companies TEXT[] := ARRAY ['GOOG', 'YHOO', 'MSFT', 'AAPL', 'INTC', 'ORCL', 'ORLY', 'EBAY'];
 _company TEXT;
 _week INT;

BEGIN
   FOREACH _company IN ARRAY _all_companies LOOP
     INSERT INTO StockQuotes(company, week, share_price)
     VALUES (_company, 0, (random()*500)::INT);
   END LOOP;
   FOR _week IN 1..50 LOOP
     INSERT INTO StockQuotes(company, week, share_price)
     SELECT company, _week, share_price + (random()*100 - 50)::INT
     FROM StockQuotes
     WHERE week = _week - 1;
   END LOOP;
 END;
 $$ LANGUAGE plpgsql;

 SELECT GenerateData();
