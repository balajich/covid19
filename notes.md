# Environment
    source ~/.local/bin/virtualenvwrapper.sh
    source ~/.bashrc
    mkvirtualenv cv19 -p python3
    workon cv19
    pip install numpy
    pip install pandas
    pip install spyder
    pip install matplotlib
# Run
python extract_train_evaluvate.py
python recognize_faces.py --image ./recognize-images/kate_leonardo.jpg