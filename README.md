# verbnet_interface
 This code can easily use verbnet resources (https://www.nltk.org/_modules/nltk/corpus/reader/verbnet.html) like WordNet's synset. This imitates WordNet's synset function.
 
 # example
 It is the same as example_usage.ipynb
 ```
 from verbnet_interface.verbnet_interface import verbnet_interface as vi
 vn_say = vi("say")
 print(vn_say.synsets[1].get_wordnetids())
 # example_output
 # [Synset('announce.v.01'), Synset('announce.v.03'), ..., Synset('report.v.02')]
 ```
 
 # Thank you for reading
If this program is helpful for you, I want you to give the star this program for me because it leads to assist looking for my job. Have a nice day.
 
