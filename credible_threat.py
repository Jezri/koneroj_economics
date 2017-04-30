from koneroj import*
credible_threat = writable_concept("Credible threat")
credible_threat.parts["Definition"].desplay += r''' A threat is credible if it is the probable action of a player. This may happen in three different circumstances.
\begin{enumerate}
\item The threat is preset to happen with no chioce of the player after they have set the threat.
\item The threatened action is still optimal after the action it was intended to prevent has occured.
\item The player is irrational.
\end{enumerate}'''

credible_threat.write_module_doc()
