# working with scikit-learn for ML
import graphviz
import inline as inline
import matplotlib
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
# tree.plot_tree(clf.fit(iris.data, iris.target))
# dot_data = tree.export_graphviz(clf, out_file=iris.pdf)
# graph = graphviz.Source(dot_data)
# graph.render("iris")
