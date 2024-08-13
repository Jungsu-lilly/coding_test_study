# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict

def solution(word, pages):
    word = word.lower()
    basic_scores = []
    link_dict = defaultdict(list)
    page_dict = {}

    def get_base_url(page):
        temp = '<meta property="og:url" content="'
        meta_start = page.find(temp) + len(temp)
        meta_end = page.find('"', meta_start)
        return page[meta_start:meta_end]

    def get_linked_urls(page):
        links = []
        pos = page.find('<a href="')
        while pos != -1:
            start = pos + len('<a href="')
            end = page.find('"', start)
            links.append(page[start:end])
            pos = page.find('<a href="', end)
        return links

    def get_basic_score(page, word):
        lower_page = page.lower()
        score = 0
        pos = lower_page.find(word)
        while pos != -1:
            if (pos == 0 or not lower_page[pos - 1].isalpha()) and (pos + len(word) == len(lower_page) or not lower_page[pos + len(word)].isalpha()):
                score += 1
            pos = lower_page.find(word, pos + len(word))
        return score

    for idx, page in enumerate(pages):
        base_url = get_base_url(page)
        page_dict[base_url] = idx

        basic_score = get_basic_score(page, word)
        basic_scores.append(basic_score)

        linked_urls = get_linked_urls(page)
        for link in linked_urls:
            link_dict[link].append(base_url)

    link_scores = [0] * len(pages)

    for link, from_urls in link_dict.items():
        if link in page_dict:
            link_index = page_dict[link]
            for from_url in from_urls:
                if from_url in page_dict:
                    from_index = page_dict[from_url]
                    link_scores[link_index] += basic_scores[from_index] / len(get_linked_urls(pages[from_index]))

    total_scores = [basic_scores[i] + link_scores[i] for i in range(len(pages))]

    answer = total_scores.index(max(total_scores))
    return answer


