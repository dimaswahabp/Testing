{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 9.1 `lambda` function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = lambda a:a\n",
    "x(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Kapan kita pakai lambda adalah ketika kita butuh function untuk satu variabel saja"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y =lambda a,b,c : a+b+c\n",
    "y(2,5,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n",
      "64\n",
      "1024\n"
     ]
    }
   ],
   "source": [
    "def my_function(x):\n",
    "    return lambda a:a**x\n",
    "\n",
    "pangkat2 = my_function(2)\n",
    "pangkat3 = my_function(3)\n",
    "pangkat5 = my_function(5)\n",
    "\n",
    "print(pangkat2(4))\n",
    "print(pangkat3(4))\n",
    "print(pangkat5(4))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "kita dapat membuat fungsi turunan dengan menggunakan lambda function. Seperti contoh di atas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "y = lambda a : True if a%2 == 0 else False\n",
    "print(y(2))\n",
    "print(y(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Angka Genap\n",
      "Angka Ganjil\n"
     ]
    }
   ],
   "source": [
    "y = lambda a : 'Angka Genap' if a%2 == 0 else 'Angka Ganjil'\n",
    "print(y(2))\n",
    "print(y(3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 9.2 `map` function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 4, 4]\n"
     ]
    }
   ],
   "source": [
    "def y(a):\n",
    "    return len(a)\n",
    "\n",
    "a = ['Andi', 'Budi', 'Caca']\n",
    "x = map(y, a)\n",
    "print(list(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Cokelat Apel', ' Melon Jeruk', 'Nangka Nanas']\n"
     ]
    }
   ],
   "source": [
    "a = ['Cokelat', ' Melon', 'Nangka']\n",
    "b = ['Apel', 'Jeruk', 'Nanas']\n",
    "def combi(a, b):\n",
    "    return a+' '+b\n",
    "\n",
    "x = map(combi, a, b)\n",
    "print(list(x))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 9.3 `filter` function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 6, 7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "x = range(11)\n",
    "def kurang_lima(a):\n",
    "    if a < 5:\n",
    "        return False\n",
    "    else:\n",
    "        return True\n",
    "    \n",
    "y = filter(kurang_lima, x)\n",
    "print(list(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2]\n"
     ]
    }
   ],
   "source": [
    "x = [1,2,3,4,5]\n",
    "y = [1,2,6,7,8]\n",
    "\n",
    "z = filter(lambda a: a in x, y)\n",
    "print(list(z))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9.4 `reduce` function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "from functools import reduce"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "number = [1,2,3,4]\n",
    "y = reduce(lambda a, b:a*b, number)\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "number = [1,2,3,4]\n",
    "hasil = 1\n",
    "for i in number:\n",
    "    hasil *= i\n",
    "\n",
    "print(hasil)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iniibubudi\n"
     ]
    }
   ],
   "source": [
    "kata = ['ini', 'ibu', 'budi']\n",
    "b = reduce(lambda a, b:a+b, kata)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9.5 `map` x `filter`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[8]\n",
      "[4, 6, 8]\n"
     ]
    }
   ],
   "source": [
    "angka = [1,2,3,4]\n",
    "\n",
    "z = list(map(lambda x:x*2, filter(lambda x:x>3, angka)))\n",
    "y = list(filter(lambda x:x>3, map(lambda x:x*2, angka)))\n",
    "print(z)\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9.6.1 Quiz 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 16, 36, 64]\n"
     ]
    }
   ],
   "source": [
    "x = [2, 4, 6, 8]\n",
    "def power(a):\n",
    "    return a**2\n",
    "\n",
    "y = map(power, x)\n",
    "print(list(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 16, 36, 64]\n"
     ]
    }
   ],
   "source": [
    "x = [2, 4, 6, 8]\n",
    "y = map(lambda a:a**2, x)\n",
    "print(list(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 16, 36, 64]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = [2, 4, 6, 8]\n",
    "b = [a**2 for a in x]\n",
    "b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9.6.2 Quiz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5100"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num_list = list(range(1,101))\n",
    "mantap = reduce(lambda x,y:x+y, map(lambda x:x*2, filter(lambda x:x%2==0, num_list)))\n",
    "print(num_list)\n",
    "mantap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]\n",
      "[0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num_list = list(range(1,101))\n",
    "even = [i%2==0 for i in num_list]\n",
    "even_2 = [i*2 for i in even]\n",
    "sum_even = sum(even_2)\n",
    "print(even)\n",
    "print(even_2)\n",
    "sum_even"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"
     ]
    }
   ],
   "source": [
    "num_list = list(range(0,100))\n",
    "prime = list(filter(lambda x:x%11!=0 or x==11,\n",
    "                    filter(lambda x:x%7!=0 or x==7,\n",
    "                           filter(lambda x:x%5!=0 or x==5,\n",
    "                                  filter(lambda x:x%3!=0 or x==3,\n",
    "                                         filter(lambda x:x%2!=0 or x==2,\n",
    "                                                filter(lambda x:x>1, num_list)))))))\n",
    "print(prime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "coba = 'apakabar'\n",
    "len_coba = len(coba)\n",
    "len_coba"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
