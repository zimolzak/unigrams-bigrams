.PHONY: analytics
analytics : pride_prej.txt ngrams.py
	python ngrams.py

pride_prej.txt : pride_prej_gute.txt
	tail -n +32 pride_prej_gute.txt | head -n 13034 > $@

pride_prej_gute.txt :
	curl https://www.gutenberg.org/files/1342/1342-0.txt -o $@

clean :
	rm pride_prej.txt
