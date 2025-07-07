# Daub 5/3 integer-to-integer system
## Lifting forms

В случае вектора ${f}$ размера ${N}$ коэффициенты разложения Daub 5/3 при ${k=[1;N]}$:

$$\begin{align}
    d_k &= \cfrac{-1}{2} f_{2k-1} + f_{2k} + \cfrac{-1}{2} f_{2k+1}, \\
    a_k &= \cfrac{-1}{8} f_{2k-3} + \cfrac{1}{4} f_{2k-2} + \cfrac{3}{4} f_{2k-1} + \cfrac{1}{4} f_{2k} + \cfrac{-1}{8} f_{2k+1},
\end{align}$$

где $d$ - флуктуации, $a$ - тренд.

С учетом

$$\begin{equation}
    d_{k-1} = \cfrac{-1}{2} f_{2k-3} + f_{2k-2} + \cfrac{-1}{2} f_{2k-1},
\end{equation}$$

сумма

$$\begin{equation}
    \left( d_{k-1} + d_{k} \right) = \cfrac{-1}{2} f_{2k-3} + f_{2k-2} + (-1) f_{2k-1} + f_{2k} + \cfrac{-1}{2} f_{2k+1}.
\end{equation}$$

Таким образом, коэффициенты ${a_k}$ можно представить следующей линейной комбинацией:

$$\begin{equation}
    a_k = f_{2k-1} + \cfrac{1}{4} \left( d_{k-1} + d_{k} \right).
\end{equation}$$

Результирующие выражения для ${d_k}$ и ${a_k}$ при ${k=[1;N]}$:

$$\begin{align}
    d_k &= f_{2k} - \cfrac{1}{2} \left( f_{2k-1} + f_{2k+1} \right), \\
    a_k &= f_{2k-1} + \cfrac{1}{4} \left( d_{k-1} + d_{k} \right).
\end{align}$$

В случае индексации от ${k=0}$ ${\left( f_k \rightarrow f_{k+1} \right)}$ выражения принимают вид:

$$\begin{align}
    d_k &= f_{2k+1} - \cfrac{1}{2} \left( f_{2k} + f_{2k+2} \right), \\
    a_k &= f_{2k} + \cfrac{1}{4} \left( d_{k-1} + d_{k} \right).
\end{align}$$

Исходные формулы в случае индексации от ${k=0}$ ${\left( f_k \rightarrow f_{k+1} \right)}$:

$$\begin{align}
    d_k &= \cfrac{-1}{2} f_{2k} + f_{2k+1} + \cfrac{-1}{2} f_{2k+2}, \\
    a_k &= \cfrac{-1}{8} f_{2k-2} + \cfrac{1}{4} f_{2k-1} + \cfrac{3}{4} f_{2k} + \cfrac{1}{4} f_{2k+1} + \cfrac{-1}{8} f_{2k+2}.
\end{align}$$

# Reference
1. [Calderbank A.R. Wavelet transforms that map integers to integers // Applied and Computational Harmonic Analysis Volume 5, Issue 3, July 1998, Pages 332-369.](https://www.sciencedirect.com/science/article/pii/S1063520397902384)
2. [Wim Sweldens. The Lifting Scheme: A Custom-Design Construction of Biorthogonal Wavelets // Applied and Computational Harmonic Analysis Volume 3, Issue 2, April 1996, Pages 186-200.](https://www.sciencedirect.com/science/article/pii/S1063520396900159)