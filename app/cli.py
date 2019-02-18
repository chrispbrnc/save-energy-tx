'''
Flask CLI setup

Commands:
    frontend -- for managing frontend assets
    test     -- run tests
'''
import os
import unittest

def register(app):
    @app.cli.group()
    def frontend():
        """Build Frontend assets"""
        pass

    @frontend.command()
    def build():
        """Build Files"""
        if os.system('npm run build'):
            raise RuntimeError('build command failed')

    @frontend.command()
    def watch():
        """Watch files, build on change"""
        if os.system('npm run watch'):
            raise RuntimeError('watch command failed')

    @frontend.command()
    def clean():
        """Clean build files"""
        if os.system('npm run clean'):
            raise RuntimeError('clean command failed')

    @app.cli.group()
    def test():
        """Run App tests"""
        pass

    @test.command()
    def all():
        """Run all tests"""
        tests = unittest.TestLoader().discover('app/tests', pattern='test_*.py')
        unittest.TextTestRunner(verbosity=2).run(tests)
