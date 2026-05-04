from app import create_app

# Punto de entrada principal para ejecutar la aplicacion con Flask.
app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
