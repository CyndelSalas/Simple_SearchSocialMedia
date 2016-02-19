import webbrowser
new=2
tabUrl="https://www.google.com/search?safe=active&site=webhp&source=hp&q=";
martindale="http://www.martindale.com/Results.aspx?ft=1&frm=freesearch&afs=";
term=raw_input("Enter text:  ");
webbrowser.open(martindale+term, new=new);
webbrowser.open(tabUrl+term+" site:avvo.com", new=new);
webbrowser.open(tabUrl+term+" site:linkedin.com", new=new);
webbrowser.open(tabUrl+term+" site:lawyers.com", new=new);
#webbrowser.open(tabUrl+term+" site:martindale.com", new=new);