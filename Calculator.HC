// Calculator in HolyC.
// Supports + - * / ^, parentheses and unary minus.
// Type an expression at the prompt. Empty line quits.

Bool calc_err;

F64 CalcExpr(U8 **_s);
F64 CalcUnary(U8 **_s);

U0 SkipWhite(U8 **_s)
{
  while (**_s==' ' || **_s=='\t')
    (*_s)++;
}

F64 CalcAtom(U8 **_s)
{
  F64 res;
  U8 *end;
  SkipWhite(_s);
  if (**_s=='(') {
    (*_s)++;
    res=CalcExpr(_s);
    SkipWhite(_s);
    if (**_s==')')
      (*_s)++;
    else
      calc_err=TRUE;
    return res;
  }
  res=Str2F64(*_s,&end);
  if (end==*_s)
    calc_err=TRUE;
  *_s=end;
  return res;
}

// ^ is right-associative and binds tighter than unary minus: -2^2 = -4
F64 CalcPower(U8 **_s)
{
  F64 base=CalcAtom(_s);
  SkipWhite(_s);
  if (**_s=='^') {
    (*_s)++;
    return Pow(base,CalcUnary(_s));
  }
  return base;
}

F64 CalcUnary(U8 **_s)
{
  SkipWhite(_s);
  if (**_s=='-') {
    (*_s)++;
    return -CalcUnary(_s);
  }
  return CalcPower(_s);
}

F64 CalcTerm(U8 **_s)
{
  F64 res=CalcUnary(_s),rhs;
  while (TRUE) {
    SkipWhite(_s);
    if (**_s=='*') {
      (*_s)++;
      res*=CalcUnary(_s);
    } else if (**_s=='/') {
      (*_s)++;
      rhs=CalcUnary(_s);
      if (rhs==0)
        calc_err=TRUE;
      else
        res/=rhs;
    } else
      return res;
  }
}

F64 CalcExpr(U8 **_s)
{
  F64 res=CalcTerm(_s);
  while (TRUE) {
    SkipWhite(_s);
    if (**_s=='+') {
      (*_s)++;
      res+=CalcTerm(_s);
    } else if (**_s=='-') {
      (*_s)++;
      res-=CalcTerm(_s);
    } else
      return res;
  }
}

U0 Calc()
{
  U8 *line,*s;
  F64 res;
  "HolyC Calculator. Empty line quits.\n";
  while (TRUE) {
    line=GetStr("> ");
    if (!*line) {
      Free(line);
      break;
    }
    calc_err=FALSE;
    s=line;
    res=CalcExpr(&s);
    SkipWhite(&s);
    if (*s)
      calc_err=TRUE;
    if (calc_err)
      "Error\n";
    else
      "= %f\n",res;
    Free(line);
  }
}

Calc;
