
CREATE TABLE user (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	email VARCHAR(150) NOT NULL, 
	password_hash VARCHAR(128) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);

INSERT INTO user VALUES(1,'user@example.com','pbkdf2:sha256:260000$0L3PwFdvPNkXWPqs$e92e46bbdc90e16c1717ea668281b9f669e8454ae3a68537daa24d7bc8add707');


CREATE TABLE product (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(100) NOT NULL, 
	description TEXT NOT NULL, 
	price FLOAT NOT NULL, 
	product_image_url VARCHAR(255) NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);

INSERT INTO product VALUES(1,'Product Name','Product Description',20.0,'http://example.com/image.jpg',1);
INSERT INTO product VALUES(2,'Product 2','Product Description',4.0,'http://example.com/image.jpg',2);

CREATE TABLE category (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(100) NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);

INSERT INTO category VALUES(1, 'Category 1', 'Description for category 1');
INSERT INTO category VALUES(2, 'Category 2', 'Description for category 2');

CREATE TABLE `order` (
	id VARCHAR(36) NOT NULL, 
	email VARCHAR(150) NOT NULL, 
	status VARCHAR(50), 
	items JSON NOT NULL, 
	payment_id VARCHAR(100), 
	PRIMARY KEY (id)
);

INSERT INTO `order` VALUES('48886654-b69f-4c6d-a706-f2bc8287adea','pooja.prp99@gmail.com','Pending','[{"product_id": 1, "quantity": 2}]','PAYID-M2YREXY3KA62561TD2276146');
INSERT INTO `order` VALUES('008ee5f1-d2a0-4982-b919-4f754f1bd0cf','pooja.prp99@gmail.com','Pending','[{"product_id": 1, "quantity": 2}]',NULL);
INSERT INTO `order` VALUES('40af56b3-63d3-4048-857c-c81f19fea182','pooja.prp99@gmail.com','Paid','[{"product_id": 1, "quantity": 2}]',NULL);
INSERT INTO `order` VALUES('3f35c30f-4736-444e-928d-dc5edd5846bf','pooja.prp99@gmail.com','Paid','[{"product_id": 1, "quantity": 2}]',NULL);
INSERT INTO `order` VALUES('b449ed88-3b60-4ed3-9202-6a3736475d2f','pooja.prp99@gmail.com','Pending','[{"product_id": 1, "quantity": 2}]',NULL);
INSERT INTO `order` VALUES('9267ac42-8ecc-4a34-bf54-73e3f3b179de','user@example.com','Paid','[{"product_id": 2, "quantity": 2}]',NULL);
INSERT INTO `order` VALUES('253c8d92-18a6-43da-830d-43fdd0a1941c','user@example.com','Paid','[{"product_id": 2, "quantity": 2}]','440e1ba7-7706-4abf-a15b-8295f8d2a0ef');


CREATE TABLE inventory (
	product_id INTEGER NOT NULL, 
	stock INTEGER NOT NULL, 
	PRIMARY KEY (product_id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);

INSERT INTO inventory VALUES(1,89);
INSERT INTO inventory VALUES(2,1);

COMMIT;
