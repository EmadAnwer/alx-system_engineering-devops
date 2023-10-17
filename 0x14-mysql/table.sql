# Create a database named tyrell_corp.
CREATE DATABASE  IF NOT EXISTS tyrell_corp;

USE tyrell_corp;

# Create a table named replicants with the following columns:
# - id, an integer that is the primary key
# - name, a string

CREATE TABLE nexus6 (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255)
);

# Insert the following replicants into the table:
# - Emad
# - Ali

INSERT INTO nexus6 (name) VALUES ('Leon');
INSERT INTO nexus6 (name) VALUES ('Ali');


#CHANGE MASTER TO MASTER_HOST = '', MASTER_USER = 'replica_user', MASTER_PASSWORD = '', MASTER_LOG_FILE = 'mysql-bin.000744', MASTER_LOG_POS = 4133;
