# SuperSet for Piattaforma Digitale Nazionale Dati (PDND), previously DAF

Superset is a Business Intelligence open source web application, originally developed by AirBnB. With SuperSet you can create charts ("slices" following the SuperSet terminology), expose dashboards and execute SQL queries.

Superset has been integrated within the PDND projectto offer users the ability to create own analysis and share them with the rest of the community.

## What is the PDND (previously DAF)?

PDND stays for "Piattaforma Digitale Nazionale Dati" (the Italian Digital Data Platform), previously known as Data & Analytics Framework (DAF).

You can find more informations about the PDND on the official [Digital Transformation Team website](https://teamdigitale.governo.it/it/projects/daf.htm).

### Project components *(optional)*

Superset makes use of the following additional components (download from other repositories).

* **Redis** version 5.0.5. Redis is automatically pulled in as a dependency from its [official Docker repository](https://hub.docker.com/_/redis).

* **PostgreSQL** version 10.9. Postgres is automatically pulled in as a dependency from its [official Docker repository](https://hub.docker.com/_/postgres).

## How to build and test Superset

In this repository, Superset and its related tools are redistributed as a set of Docker containers interacting with one each other.

The `dockerfile` and the `docker-compose.yaml` files are in the root of this repository.

To build the local test environment (build the Superset container and download dependencies) run:

```shell
docker-compose up -d
```

>NOTE: the `docker-compose.yaml` file sets different environment variables that could be used to adapt and customized many platform functionalities.

Then, access the CKAN GUI in a browser at `http://localhost:8088`.

To bring down the test environment and remove the containers use

```shell
docker-compose down
```

## How to contribute

Contributions are welcome. Feel free to [open issues](./issues) and submit a [pull request](./pulls) at any time, but please read [our handbook](https://github.com/teamdigitale/daf-handbook) first.

## License

Copyright (c) 2019 Presidenza del Consiglio dei Ministri

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
