{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9b589460-bd77-42e0-a2e1-08b4ad1f4bfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f4e5c938-681e-4271-8d71-346e803b1d0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "marks = np.array([60,50,40])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "55bb7888-8c6a-4db6-8952-11705e08befb",
   "metadata": {},
   "outputs": [],
   "source": [
    "su = marks.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "18b05dc6-70cf-42ea-b806-937917c9927a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "150\n"
     ]
    }
   ],
   "source": [
    "print(su)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "17c8e369-734d-4c01-b299-4628d73cd506",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50.0\n"
     ]
    }
   ],
   "source": [
    "print(marks.mean())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3bbc3bc9-1227-4f57-b0a4-d0f8259617ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8.16496580927726\n"
     ]
    }
   ],
   "source": [
    "print(marks.std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8f107b7d-3fe6-4d06-a0be-fdf8ea1f1f12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "60\n"
     ]
    }
   ],
   "source": [
    "print(marks.max())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58b631dd-57e4-4895-9731-1f94e99c69eb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4accc9b3-2a26-4967-9765-aa2d4024df38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40\n"
     ]
    }
   ],
   "source": [
    "print(marks.min())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "90ad508f-d6bd-4761-8490-d369afef695b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[60]\n",
      " [50]\n",
      " [40]]\n"
     ]
    }
   ],
   "source": [
    "print(marks.reshape(3,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "13ddf99b-aaff-43ac-9363-d7609402da88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[40 50 60]\n"
     ]
    }
   ],
   "source": [
    "print(np.sort(marks))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a356ad15-2700-4b1c-b182-7be775ab0b1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n"
     ]
    }
   ],
   "source": [
    "print(marks[0]+marks[2])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
