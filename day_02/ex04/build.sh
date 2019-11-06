mkdir ai42
cp loging.log.py ai42/.
cp progressbar.py ai42/.
touch ai42/__init__.py
echo "import ai42" >> ai42/__init__.py
echo "from ai42.progressbar import ft_progress" >> ai42/__init__.py
echo '__version__ = "1.0.0"' >> ai42/__init__.py
#tar -cvf ai42-1.0.0.tar.gz setup.py ai42/*.py
#mkdir dist
#mv ai42-1.0.0.tar.gz dist/.
#rm -Rf ai42