from src.settings import BASE_DIR, env


class TestSettings:
    def test_base_dir(self):
        assert BASE_DIR.exists()

    def test_load_env(self):
        debug = env.get_value("DEBUG")
        assert debug is True
