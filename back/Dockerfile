FROM rust:buster

RUN apt-get update && apt-get upgrade -y
RUN apt-get install vim git -y

# create a default cargo project to complete the setup
RUN cd /home && export USER=root && cargo new back --bin
WORKDIR /home/back

# configs for using rocket.rs
RUN rustup default nightly
RUN rustup override set nightly
EXPOSE 8080
# update rust packages
RUN rustup update && cargo update

# add rocket dependency
COPY ./Cargo.toml /home/back/
# copy default Rocket server (replaces existing main.rs)
COPY ./src/*.rs /home/back/src/main.rs
COPY ./database/* /home/back/database/
# build the Rocket server dependencies
RUN cargo build
ENV ROCKET_ADDRESS=0.0.0.0
ENV ROCKET_PORT=8080
# copy Rocket default settings (req to set Docker-compliant host)
COPY ./Rocket.toml /home/back/Rocket.toml

CMD ["cargo", "run"]