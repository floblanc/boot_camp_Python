cd /sgoinfre/goinfre/Perso &&
mkdir -p $USERNAME &&
chmod 700 $USERNAME &&
cd $USERNAME &&
curl -o miniconda3.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh &&
sh miniconda3.sh -b -p miniconda3 &&
echo "export PATH=\"/sgoinfre/goinfre/Perso/$USERNAME/miniconda3/bin:\$PATH\"" >> ~/.zshrc
