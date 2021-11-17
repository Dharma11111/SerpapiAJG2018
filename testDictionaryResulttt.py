from typing_extensions import _AnnotatedAlias
from numpy.lib.stride_tricks import as_strided
from numpy.testing._private.utils import assert_array_almost_equal
from BasicCommands import *

resulttt = {
#region #Sample Data

'search_metadata'       : 
	{
	'id'                : '618fb627a74fe0fa2ad905f3', 
    'status'            : 'Success', 
    'json_endpoint'     : 'https://serpapi.com/searches/e6cf9ad681027ac4/618fb627a74fe0fa2ad905f3.json', 
    'created_at'        : '2021-11-13 12:57:11 UTC', 
    'processed_at'      : '2021-11-13 12:57:11 UTC', 
    'google_scholar_url': 'https://scholar.google.com/scholar?q=%27csr%27+OR+%27financial+distress%27&hl=en&start=10&num=1&as_ylo=2018', 
    'raw_html_file'     : 'https://serpapi.com/searches/e6cf9ad681027ac4/618fb627a74fe0fa2ad905f3.html', 
    'total_time_taken'  : 0.89
    }, 
'search_parameters'     : 
    {
    'engine'            : 'google_scholar', 
    'q'                 : "'csr' OR 'financial distress'", 
    'hl'                : 'en', 
    'start'             : 10, 
    'num'               : '1', 
    'as_ylo'            : '2018'
    }, 
'search_information'    : 
    {
    'organic_results_state'     : 'Results for exact spelling', 
    'total_results'             : 114000, 
    'page_number'               : 11, 
    'time_taken_displayed'      : 0.05, 
    'query_displayed'           : "'csr' OR 'financial distress'"
    }, 
'organic_results'       : 
    [
        {
        'position'              : 0, 
        'title'                 : 'The influence of liquidity, leverage and profitability on financial distress of listed manufacturing companies in Indonesia', ###
        'result_id'             : 'j08HAVILCPwJ', 
        'type'                  : 'Pdf', 
        'link'                  : 'https://www.atlantis-press.com/article/25902682.pdf', ### source pilih yg ada di lms
        'snippet'               : 'This research aims to empirically examine the influence of (1) liquidity,(2) leverage and (3) profitability on financial distress of manufacturing companies listed in Indonesian Stock Exchange (IDX). The population in this study are all manufacturing companies listed in …', 
        'publication_info'      : 
            {
            'summary'           : 'E Masdupi, A Tasman, A Davista - Advances in Economics …, 2018 - atlantis-press.com', 
            'authors'           : 
            [
                {
                'name'                  : 'A Tasman', 
                'link'                  : 'https://scholar.google.com/citations?user=OztLHhoAAAAJ&hl=en&num=1&oi=sra', 
                'serpapi_scholar_link'  : 'https://serpapi.com/search.json?author_id=OztLHhoAAAAJ&engine=google_scholar_author&hl=en', 
                'author_id'             : 'OztLHhoAAAAJ'
                }
            ]
            }, 
        'resources'             : 
            [
                {
                'title'         : 'atlantis-press.com', 
                'file_format'   : 'PDF', 
                'link'          : 'https://www.atlantis-press.com/article/25902682.pdf'
                }
            ], 
        'inline_links'          : 
            {
            'serpapi_cite_link'     : 'https://serpapi.com/search.json?engine=google_scholar_cite&q=j08HAVILCPwJ', 
            'cited_by'              : 
                {
                'total'                 : 46, 
                'link'                  : 'https://scholar.google.com/scholar?cites=18160777944204005263&as_sdt=4005&sciodt=0,6&hl=en&num=1', 
                'cites_id'              : '18160777944204005263', 
                'serpapi_scholar_link'  : 'https://serpapi.com/search.json?as_sdt=4005&cites=18160777944204005263&engine=google_scholar&hl=en&num=1'
                }, 
            'related_pages_link'    : 'https://scholar.google.com/scholar?q=related:j08HAVILCPwJ:scholar.google.com/&scioq=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
            'versions'              : 
                {
                'total'                 : 2, 
                'link'                  : 'https://scholar.google.com/scholar?cluster=18160777944204005263&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
                'cluster_id'            : '18160777944204005263', 
                'serpapi_scholar_link'  : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&cluster=18160777944204005263&engine=google_scholar&hl=en&num=1'
                }, 
            'cached_page_link'          : 'https://scholar.googleusercontent.com/scholar?q=cache:j08HAVILCPwJ:scholar.google.com/+%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018'
            }
        }
    ], 
'pagination'        : 
    {
    'current'       : 11, 
    'previous'      : 'https://scholar.google.com/scholar?start=9&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
    'next'          : 'https://scholar.google.com/scholar?start=11&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
    'other_pages'   : 
        {
        '6'         : 'https://scholar.google.com/scholar?start=5&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '7'         : 'https://scholar.google.com/scholar?start=6&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '8'         : 'https://scholar.google.com/scholar?start=7&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '9'         : 'https://scholar.google.com/scholar?start=8&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '10'        : 'https://scholar.google.com/scholar?start=9&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '12'        : 'https://scholar.google.com/scholar?start=11&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '13'        : 'https://scholar.google.com/scholar?start=12&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '14'        : 'https://scholar.google.com/scholar?start=13&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018', 
        '15'        : 'https://scholar.google.com/scholar?start=14&q=%27csr%27+OR+%27financial+distress%27&hl=en&num=1&as_sdt=0,6&as_ylo=2018'
        }
    }, 
    'serpapi_pagination'    : 
        {
        'current'       : 11, 
        'previous_link' : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=9', 
        'previous'      : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=9', 
        'next_link'     : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=11', 
        'next'          : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=11', 
        'other_pages'   : 
            {
            '6'     : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=5', 
            '7'     : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=6', 
            '8'     : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=7', 
            '9'     : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=8', 
            '10'    : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=9', 
            '12'    : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=11', 
            '13'    : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=12', 
            '14'    : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=13', 
            '15'    : 'https://serpapi.com/search.json?as_sdt=0%2C6&as_ylo=2018&engine=google_scholar&hl=en&num=1&q=%27csr%27+OR+%27financial+distress%27&start=14'
            }
        }
    }

#endregion

#region #list & print
listSourceLms = ['emerald','jstor','proquest','sciencedirect','wiley']
listBadRating = []

googleScholarUrl = resulttt['search_metadata']['google_scholar_url']

## list index 0 berarti hasil search yg ke 1
listIndex   = []
listTitle   = []
title       = resulttt['organic_results'][0]['title'] 
listLink    = []
link        = resulttt['organic_results'][0]['link']
listSnippet = []
snippet     = resulttt['organic_results'][0]['snippet']
listSummary = []
summary     = resulttt['organic_results'][0]['publication_info']['summary']
#title dak penting kalau bs di link
listCitedBy = []
citedBy     = resulttt['organic_results'][0]['inline_links']['cited_by']['total']
listSource  = []
listAllInfo = [listTitle,listLink,listSnippet,listCitedBy]

# print(googleScholarUrl)
# print(title)
# print(link)
# print(snippet)
# print(summary)
# print(citedBy)

#endregion

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def collectJournal(varName):
    Url = varName['search_metadata']['google_scholar_url']
    for x in range(len(varName['organic_results'])):
        listIndex.insert(x,'')
        listTitle.insert(x,'')
        listLink.insert(x,'')
        listSnippet.insert(x,'')
        listSummary.insert(x,'')
        listCitedBy.insert(x,'')
        listSource.insert(x,'')
    
    for y in listSourceLms:
        for x in range(len(varName['organic_results'])):
            print(y,x)
            try:
                if y in varName['organic_results'][x]['link']:
                    print("ada")
                    listIndex[x]        = x
                    listTitle[x]        = varName['organic_results'][x]['title']
                    listLink[x]         = varName['organic_results'][x]['link']
                    listSnippet[x]      = varName['organic_results'][x]['snippet']
                    # tempSummaryVariable = varName['organic_results'][x]['publication_info']['summary']                       # sebelum rating jurnal di cut
                    # listSummary[x]      = tempSummaryVariable[find_nth(tempSummaryVariable,'-',1):find_nth(tempSummaryVariable,'-',2)-6]    # setelah rating jurnal di cut, ga bs cut karna ada nama penulis pake '-'
                    listSummary[x]      = varName['organic_results'][x]['publication_info']['summary']  
                    listCitedBy[x]      = varName['organic_results'][x]['inline_links']['cited_by']['total']
                    listSource[x]       = y

                else:
                    print('tidak ada')
            except:
                pass
    print('creating list in 3 secs')
    time.sleep(3)
    
    print('listIndex = ',listIndex)
    print('listTitle = ',listTitle)
    print('listLink = ',listLink)
    print('listSnippet = ',listSnippet)
    print('listSummary = ',listSummary)
    print('listCitedBy = ',listCitedBy)
    print('listSource = ',listSource)
    
    write("GoogleScholarUrl = '")
    write(Url)
    write("'")
    escc()
    enterr()
    write('listIndex = ')
    write(listIndex)
    escc()
    enterr()
    write('listTitle = ')
    write(listTitle)
    escc()
    enterr()
    write('listLink = ')
    write(listLink)
    escc()
    enterr()
    write('listSnippet = ')
    write(listSnippet)
    escc()
    enterr()
    write('listSummary = ')
    write(listSummary)
    escc()
    enterr()
    write('listCitedBy = ')
    write(listCitedBy)
    escc()
    enterr()
    write('listSource = ')
    write(listSource)
    escc()
    enterr()
    




# collectJournal(resulttt)

       
        

    




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~