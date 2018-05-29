# Glossary of Theoretical Terms

All definitions and section/page numbers are taken from:

_Information Flow: The Logic of Distributed Systems_. Jon Barwise and Jerry Seligman. Cambridge University Press, 1997.


## Classification
###### (Section 2.1, Page 28)
###### (Section 4.1, Page 69)

A _classification_ `A := < tok(A), typ(A), |=  >` consists of:

- A set `tok(A)` of objects called _tokens_;
- A set `typ(A)` of objects called _types_;
- A binary relation `|=` of _validity_ on `tok(A) X typ(A)`;

The relation `x |= alpha` reads _x has type alpha_ or _alpha is valid for x_. The inverse relation `x |!= alpha` reads _x does not have type alpha_ or _alpha is invalid for x_.


## Infomorphism
###### (Section 2.1, Page 32)
###### (Section 4.2, Page 72)

Given two [classifications](#classification):

- `A := < tok(A), typ(A), |=_A >`
- `C := < tok(C), typ(C), |=_C >`

an _infomorphism_ is a pair of functions `< f_up, f_down >` satisfying:

- `f_up : typ(A) -> typ(C)`
- `f_down : typ(C) -> typ(A)`

and the _Fundamental Infomorphism Axiom_: for all `c in tok(C)` and `alpha in typ(A)`:

```
f_down(c) |=_A alpha  <if and only if>  c |=_C f_up(alpha)
```

## Sum
###### (Section 5.1, Page 81)

Given two [classifications](#classification) `A` and `B`, the sum `A + B` is the classification such that:

- `tok(A + B)` is the Cartesian product `tok(A) X tok(B)`;
- `typ(A + B)` is the disjoint union of:
  - `{(0, alpha) for alpha in typ(A)}`
  - `{(1, beta) for beta in typ(B)}`.
- The validity relation `|=_[A+B]` is given by:

```
(a,b) |=_[A+B] (0,alpha)  <if and only if>  a |=_A alpha
(a,b) |=_[A+B] (1,beta)   <if and only if>  b |=_B beta
```
