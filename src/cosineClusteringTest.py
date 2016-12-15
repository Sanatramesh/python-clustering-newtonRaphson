'''
For Python iMTech Mid Semester Exam - 26 Sep, 2012
For Question 2
Tests cosineClustering module
'''
import unittest
from testgenDecorator import for_examples
from cosineClustering import cluster
from utils import areListsEqual

class TestNaiveCosineClustering(unittest.TestCase):
    '''
    Test class for clustering similar documents
    '''
    stopWords = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do', 'does', 'each', 'for', 'from',
                 'has', 'have', 'how', 'i', 'if', 'in', 'is', 'it', 'its', 'just', 'no', 'not', 'of', 'on', 'or',
                 'such', 'than', 'that', 'the', 'then', 'there', 'they', 'this', 'those', 'to',
                 'was', 'we', 'what', 'when', 'where', 'which', 'who', 'why', 'will', 'with', 'would', 'yes', 'you']

    stems = ['ed', 'ly', 'ing']

    threshold = 0.5

    # ======================================================================================================


    # add any other test cases that you might want to add, here - between these two separator lines


    # =======================================================================================================


    @for_examples((["data/doc01", "data/doc02", "data/doc03", "data/doc04", "data/doc05",
                    "data/doc06", "data/doc07", "data/doc08", "data/doc09", "data/doc10"],
                   [["data/doc01", "data/doc05"], ["data/doc02", "data/doc07"],
                    ["data/doc03", "data/doc06"], ["data/doc04", "data/doc08"],
                    ["data/doc09", "data/doc10"]]))
    def testClustering(self, files, clusters):
        clusters.sort()
        foundClusters = cluster(files, self.threshold, self.stopWords, self.stems)
        foundClusters.sort()
        self.assertEqual(True, areListsEqual(clusters, foundClusters))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()