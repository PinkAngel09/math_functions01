import streamlit as st
import math
st.set_page_config(page_title= '✨ AREA OF POLYGONS AND CIRCUMFERENCE ✨ | aadya', page_icon= 'me.png', layout='centered', initial_sidebar_state='auto')
st.title('✨ AREA OF POLYGONS AND CIRCUMFERENCE ✨')
def rec_area(n1, n2):
    st.success(f"The area of the rectangle/square is: { str(n1 * n2) }")


def para_area(ba, ht):
    st.success(f"The area of the paralleogram is: { str(ba * ht) }")


def tri_area (b2, ht2):
    st.success(f"The area of the triangle is: { str((b2 * ht2)/2) }")

def trap_area (len1, len2, height):
    st.success(f"The area of the trapezium is: { str(((len1+len2)*height)/2) }")

def cir_area(radius):
    st.success(f"The area of the circle is: { str((math.pi*(radius*2)))}")

def circumference(rad1):
    st.success(f"The circumference is: { str(((rad1*2)*math.pi))}")

st.success('✨This app is for calculating the areas of different polygons. Type in the number of sides for the function you would like to calculate.✨')


col1, col2 = st.beta_columns(2)
with col1:
    st.header('Area of a Rectangle/Square')
    st.text('area = length x width / side x side')
    n1 = st.number_input('Enter the length', 1)
    n2 = st.number_input('Enter the width', 1)
    rec_area(n1, n2)

with col2:
    st.header('Area of a Paralleogram')
    st.text('area = base x height')
    ba = st.number_input('Enter the base', 1)
    ht = st.number_input('Enter the height', 1)
    para_area(ba, ht)

with col1:
    st.header('Area of a Triangle')
    st.text('area = 1/2(base x height)')
    b2 = st.number_input('Enter the base:', 1)
    ht2 = st.number_input('Enter the height:', 1)
    tri_area(b2, ht2)

with col2:
    st.header('Area of a Trapezium')
    st.text('area = 1/2( (side1 + side2) x height)')
    len1 = st.number_input('Enter the side one of the trapezoid:', 1)
    len2 = st.number_input('Enter the side two of the trapezoid:', 1)
    height = st.number_input('Enter the height of the trapezoid:', 1)
    trap_area(len1, len2, height) 

st.markdown('---') # see *
st.success('✨This app is for calculating the properties of a circle. Type in the radius or diameter for the function you would like to calculate.✨')
colx, coly = st.beta_columns(2)

with colx:
    st.header('Area of a Circle')
    st.text('area = 3.14(radius * 2)')
    radius = st.number_input('Enter the radius:')
    cir_area(radius)

with coly:
    st.header('Circumference')
    st.text('area = (radius * 2) x 3.14')
    rad1 = st.number_input('Enter the Radius:')
    circumference(rad1)

st.markdown('---') # see *

st.subheader('Code for reference')
st.code('''
def rec_area(n1, n2):
    st.success(f"The area of the rectangle/square is: { str(n1 * n2) }")

def para_area(ba, ht):
    st.success(f"The area of the paralleogram is: { str(ba * ht) }")

def tri_area (b2, ht2):
    st.success(f"The area of the triangle is: { str((b2 * ht2)/2) }")

def trap_area (len1, len2, height):
    st.success(f"The area of the trapezium is: { str(((len1+len2)*height)/2) }")

def cir_area(radius):
    st.success(f"The area of the circle is: { str((math.pi*(radius*2)))}")

def circumference(rad1):
    st.success(f"The circumference is: { str(((rad1*2)*math.pi))}")
''')

st.markdown('---') # see *
st.markdown('### Author: Aadya')
