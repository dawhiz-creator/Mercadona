CREATE TABLE store (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE promo (
  id SERIAL PRIMARY KEY,
  description TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  store_id INTEGER REFERENCES store(id)
);

CREATE TABLE product (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  brand VARCHAR(255) NOT NULL,
  image_url TEXT NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE promo_product (
  promo_id INTEGER REFERENCES promo(id),
  product_id INTEGER REFERENCES product(id),
  PRIMARY KEY (promo_id, product_id)
);