# **Currency converter**

## **Description**

This application extracts information about exchange rates from [open source](https://openexchangerates.org/), stores it in its database and updates it every day (00:00 UTC). Also, the application provides an API for obtaining information on exchange rates (all currencies and filtered).

## **Instalation**

1. Install [Docker](https://docs.docker.com/install/)
2. Install [Docker Compose](https://docs.docker.com/compose/install/)
3. Clone [this repository](https://github.com/) TODO: вставить ссылку на репу
4. Open terminal and inside the downloaded repository:

```sh
docker-compose build
docker-compose up
```

4. Open new terminal window and inside the downloaded repository:

```sh
cd server
fab migrate
```

5. If you want to get access to [admin panel](<http://0.0.0.0:8000/admin/>) of app, open terminal window and inside the downloaded repository:

```sh
cd server
fab createsuperuser
```

## **Using**

This app provides following API:

* getting all existing exchange rates (<http://0.0.0.0:8000/rates/>)
* getting filtered exchange rates (<http://0.0.0.0:8000/rates/?from_cur=your_filter&to_cur=your_filter>), where `your_filter` is abbreviation of currencies, e.g. `USD`, `EUR` and so forth. List of all abbreviation you can find [here](https://www.easymarkets.com/int/learn-centre/discover-trading/currency-acronyms-and-abbreviations/)