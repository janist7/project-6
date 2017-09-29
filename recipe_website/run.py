from app import create_app, config

app = create_app(config=config.dev_config)

if __name__ == '__main__':
    app.run("0.0.0.0")
