# Glossary of Theoretical Terms

All definitions based on the exposition in:

_Information Flow: The Logic of Distributed Systems_. Jon Barwise and Jerry Seligman. Cambridge University Press, 1997.


## Classification

A _classification_ `A := < tok(A), typ(A), |=  >` consists of:

- A set `tok(A)` of objects called _tokens_;
- A set `typ(A)` of objects called _types_;
- A binary relation `|=` of _validity_ on `tok(A) X typ(A)`;

The relation `x |= alpha` reads _x has type alpha_ or _alpha is valid for x_. The inverse relation `x |!= alpha` reads _x does not have type alpha_ or _alpha is invalid for x_.

