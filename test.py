import  time 
import  unittest

da  selenio  importazione  WebDriver 
da  selenium.webdriver.common.keys  importazione  Keys


class  HackerNewsSearchTest ( unittest . TestCase ):

    def  setUp ( self ): 
         caps = {'browserName': os.getenv('BROWSER', 'chrome')}
         address = os.getenv('NODE_HUB_ADDRESS')
         self.browser = webdriver.Remote(
          command_executor='http://{address}:4444/wd/hub',
          desired_capabilities=caps
         )

    def  test_hackernews_search_for_testdrivenio ( self ): 
        browser  =  self . browser 
        browser . get ( 'https://news.ycombinator.com' ) 
        search_box  =  browser . find_element_by_name ( 'q' ) 
        search_box . send_keys ( 'testdriven.io' ) 
        search_box . send_keys ( Keys . RETURN ) 
        ora . sleep ( 3 )   # simula un test di lunga durata
        sé . assertIn ( 'testdriven.io' ,  browser . page_source )

    def  test_hackernews_search_for_selenium ( self ): 
        browser  =  self . browser 
        browser . get ( 'https://news.ycombinator.com' ) 
        search_box  =  browser . find_element_by_name ( 'q' ) 
        search_box . send_keys ( ' selenium ' ) 
        search_box . send_keys ( Keys . RETURN ) 
        ora . sleep ( 3 )   # simulano lungo in esecuzione di test 
        di auto. assertIn ( 'selenio' ,  browser . page_source )

    def  test_hackernews_search_for_testdriven ( self ): 
        browser  =  self . browser 
        browser . get ( 'https://news.ycombinator.com' ) 
        search_box  =  browser . find_element_by_name ( 'q' ) 
        search_box . send_keys ( 'testdriven' ) 
        search_box . send_keys ( Keys . RETURN ) 
        ora . sleep ( 3 )   # simula un test di lunga durata
        sé . assertIn ( 'testdriven' ,  browser . page_source )

    def  test_hackernews_search_with_no_results ( self ): 
        browser  =  self . browser 
        browser . get ( 'https://news.ycombinator.com' ) 
        search_box  =  browser . find_element_by_name ( 'q' ) 
        search_box . send_keys ( '? * ^^%' ) 
        search_box . send_keys ( Keys . RETURN ) 
        ora . sleep ( 3 )   # simulano lungo in esecuzione di test 
        di auto. assertNotIn ( '<em>' ,  browser . page_source )

    def  tearDown ( self ): 
        self . browser . quit ()   # esci vs chiudi?


if  __name__  ==  '__main__' : 
    unittest . principale ()
