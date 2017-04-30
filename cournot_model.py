from koneroj import *
cournot_model = writable_concept("Cournot model")
cournot_model.parts["Definition"].desplay += r""""Firms compete with sales volume and are interdependent.\\
These are the conditions of the basic cournot_model
\begin{enumerate}
\item Products are homogonous
\item Firms do not cooperate
\item Firms have market power
\item The number of firms is fixed
\item Firms compete in quantities, and choose quantites simulatneously
\item Firms are economically rational and act stratigically and are profit maximizing
\end{enumerate}

"""
cournot_model.write_module_doc()

