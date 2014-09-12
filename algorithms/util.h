Class Util
{
  template <class Object>
  void swap(Object &a, Object &b)
  {
    Object tmp = a;
    a = b;
    b = tmp;
  }
}
