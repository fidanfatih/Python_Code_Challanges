# https://edabit.com/challenge/yPzfgnDsPWXwH7dMq
class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = (len(items)//pageSize) + \
                           (1 if len(items) % pageSize else 0)
        self.currentPage = 1
    def getItems(self):
        return self.items
    def getPageSize(self):
        return self.pageSize
    def getCurrentPage(self):
        return self.currentPage

    # Goes to the previous page
    def prevPage(self):
        if self.currentPage != 1:
            self.currentPage -= 1
        return self

    # Goes to the next page
    def nextPage(self):
        if self.currentPage != self.totalPages:
            self.currentPage += 1
        return self

    # Goes to the first page
    def firstPage(self):
        self.currentPage = 1
        return self

    # Goes to the last page
    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    # Goes to a page determined by the `page` argument
    def goToPage(self, pageNum):
        if 1 < int(pageNum) <= self.totalPages:
            self.currentPage = int(pageNum)
        elif int(pageNum) <= 1:
            self.currentPage = 1
        else:
            self.currentPage = self.totalPages
        return self

    # Returns the currently visible items as an array
    def getVisibleItems(self):
        return self.items[(self.currentPage-1)*self.pageSize:self.currentPage*self.pageSize]
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.getVisibleItems())  # ["a", "b", "c", "d"]
p.nextPage()
print(p.getVisibleItems())  # ['e', 'f', 'g', 'h']
p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]

