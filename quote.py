class Quote:
    def __init__(self):
            self.trivia_list = [
                {
                    'trivia': 'fond of the series Brooklyn-nine-nine',
                    'member': 'Engr. SJ'
                },
                {
                    'trivia': 'watches greys anatomy and friends too !',
                    'member': 'Engr. Gabbie'
                },
                {
                    'trivia': 'fan of friends',
                    'member': 'Engr. Mae'
                },
                
                {
                    'trivia': 'loves the series House M.D',
                    'member': 'Engr. Nick'
                },
                
                {
                    'trivia': 'wants to have confidence riding on a bike and also a fan of community, (troy and abed in the morning...)',
                    'member': 'Engr. Luis'
                },
                
                {
                    'trivia': 'fan of docu-crime series',
                    'member': 'Engr. Cedie'
                },
            ]        
            
    def get_random_quote(self):
        import random    
        return random.choice(self.trivia_list)
    
    
    def get_all_quotes(self):
        return self.trivia_list

# FOR TESTING
# quote = Quote()
# random = quote.get_random_quote()
# print(random)