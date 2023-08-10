import streamlit as st
import easymodbus.modbusClientp

#----------------------------mulai fungsi ---------------------------------
#fungsi baca plc
def bacaplc():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128x = modbusclient.read_holdingregisters(64,1) #QW128 --> 40064
    modbusclient.close()
    QW128xs = "Data QW128 : " + str(QW128x)

#fungsi tulis plc
def tulisplcon():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,True)
    modbusclient.close()
def tulisplcoff():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,False)
    modbusclient.close()

def tulisplconQ02():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(2,True)
    modbusclient.close()
def tulisplcoffQ02():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(2,False)
    modbusclient.close()    
    
#----------------------------akhir fungsi ---------------------------------

st.write("""# Belajar Web dengan Python
         Ini adalah aplikasi web
          """)
#adding a button

if st.button('Siap Belajar ?'):

    st.write('Selamat Belajar') #displayed when the button is clicked
#else:
    #st.write('Have a great day') #displayed when the button is unclicked
    
if st.button('Q0.3 ON'):
    st.write(tulisplcon()) #
if st.button('Q0.3 OFF'):
    st.write(tulisplcoff()) #
