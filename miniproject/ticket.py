import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# ที่อยู่ของการเก็บข้อมูล
DATAFILE = "miniproject/DataListSellTicket.txt"

# สร้าง class Trainticket สำหรับการจัดการข้อมูลของตั๋วรถไฟฟ้า BTS สายสีเขียว
class Trainticket_BTS_GreenLine:
    def __init__(self):
        self.saleinfo = [] # ข้อมูลการขาย
        self.total_revenue = 0 # รายรับ
        self.total_change = [] # เงินทอน
    # เพิ่มข้อมูลการขายตั๋ว
    def add_sale(self, start_station, end_station,ticketprice,change):
        self.saleinfo.append((start_station,end_station,ticketprice,change))
        self.total_revenue += ticketprice #อัพเดตรายรับ
        self.total_change.append(change) #อัพเดตเงินทอนในลิส
    #funtion แสดงข้อมูลการขาย
    def display_saleinfo(self):
        return self.saleinfo 
        
    # ฟังก์ชันคำนวณราคาตั๋วรถไฟฟ้า
    def calculate_price(self, start_station, end_station):
        # สร้างพจนานุกรมที่จับคู่สถานีกับราคา
        station_prices = {
            "N24 คูคต": 15, "N23 แยก คปอ.": 15, "N22 พิพิธภัณฑ์กองทัพอากาศ": 15, "N21 โรงพยาบาลภูมิพลอดุยเดช": 15,
            "N20 สะพานใหม่": 15, "N19 สายหยุด": 15, "N18 พหลโยธิน 59": 15, "N17 วัดพระศรีมหาธาตุ": 15,
            "N16 กรมทหารราบที่ 11": 15, "N15 บางบัว": 15, "N14 กรมป่าไม้": 15, "N13 มหาวิทยาลัยเกษตรศาสตร์": 15,
            "N12 เสนานิคม": 15, "N11 รัชโยธิน": 15, "N10 พหลโยธิน 24": 15, "N9 ห้าแยกลาดพร้าว": 15,"N8 หมอชิต":15,
            "N7 สะพานควาย": 32, "N6 อารีย์": 43, "N5 สนามเป้า": 47, "N4 อนุสาวรีย์ชัยสมรภูมิ": 50 ,"N2 พญาไท":55,"N1 ราชเทวี":58
        }
        
      # ราคาพิเศษสำหรับเส้นทางที่เกี่ยวข้องกับหมอชิต
        special_prices = {
            ("N8 หมอชิต", "N7 สะพานควาย"): 17,("N8 หมอชิต", "N6 อารีย์"): 28,("N8 หมอชิต", "N5 สนามเป้า"): 32,
            ("N8 หมอชิต", "N4 อนุสาวรีย์ชัยสมรภูมิ"): 35,("N8 หมอชิต", "N2 พญาไท"): 40,("N8 หมอชิต", "N1 ราชเทวี"): 43,
            ("N8 หมอชิต", "CEN สยาม"): 47,("N8 หมอชิต", "E1 ชิดลม"): 47,("N8 หมอชิต", "E2 เพลินจิต"): 47,
            ("N8 หมอชิต", "E3 นานา"): 47,("N8 หมอชิต", "E4 อโศก"): 47,("N8 หมอชิต", "E5 พร้อมพงษ์"): 47,
            ("N8 หมอชิต", "E6 ทองหล่อ"): 47,("N8 หมอชิต", "E7 เอกมัย"): 47,("N8 หมอชิต", "E8 พระโขนง"): 47,
            ("N8 หมอชิต", "E9 อ่อนนุช"): 47
    }
            
        #เช็คว่าจุดเริ่ม เริ่มจากหมอชิตหรือไม่
        if (start_station, end_station) in special_prices:
            return special_prices[(start_station, end_station)]
        elif (end_station, start_station) in special_prices:
            return special_prices[(end_station, start_station)]

        # คำนวณราคาปกติ
        if start_station in station_prices and end_station in station_prices:
            start_price = station_prices[start_station]
            end_price = station_prices[end_station]
            return max(start_price, end_price)
        else:
            return 62  # ราคาสำหรับสถานีที่ไม่ได้อยู่ใน list ราคา



# funtion บันทึกข้อมูลการขายลงไฟล์
def save_SaleData(start_station, end_station,revenue,payment,change,countTicket):
    with open(DATAFILE,"a",encoding="utf-8")as file:
        file.write(f"{start_station},{end_station},จำนวนของตั๋ว {countTicket} ใบ ,ราคาตั๋ว{revenue},จำนวนเงินที่รับมา{payment} บาท ,เงินทอน{change} บาท \n")
        
# funtion คำนวณราคาตั๋ว
def calculate_ticketprice():
    try:
        start_station = startStation.get()
        end_station = endStation.get()
        ticketcount = int(ticketCountEntry.get())
        
        # สร้างตั๋วและคำนวณราคา
        ticketprice = ticket.calculate_price(start_station,end_station)* ticketcount
        result.config(text=f"ราคาตั๋ว : {ticketprice} บาท",fg="black")
        return ticketprice #คืนค่าราคาตั๋ว
    except ValueError:
        return None

# funtion การซื้อตั๋ว
def sellTicket():
    ticketprice = calculate_ticketprice()
    ticketcount = int(ticketCountEntry.get())
    if ticketprice is None:
        return #หยุดการทำงานเมื่อคำนวณผิดพลาด
    
    try :
        payment = float(paymentEntry.get()) #รับจำนวนเงินจากผู้ใช้
        if payment >= ticketprice: #เช็คว่า เงืนที่ใส่มามีจำนวนมากกว่า หรือเท่ากับค่าตั๋วไหม
            change =payment-ticketprice #คำนวณเงินทอน
            start_station = startStation.get()
            end_station = endStation.get()
            
            #บันทึก ข้อมูลการขายลงไฟล์
            save_SaleData(start_station, end_station,ticketprice,payment,change ,ticketcount)
            
            #แสดงราคาตั๋วและเงินทอน
            result.config(text=f"ราคาตั๋ว : {ticketprice} บาท\nเงินทอน : {change} บาท")
            
            #อัพเดต สถิติการขายใน Trainticket_BTS_GreenLine
            ticket.add_sale(start_station,end_station,ticketprice,change)
            messagebox.showinfo("การซื้อสำเร็จ", "การซื้อสำเร็จแล้ว")
        else :
            messagebox.showerror("ข้อผิดพลาด","เงินไม่เพียงพอในการซื้อตั๋ว กรุณาใส่จำนวนเงินใหม่")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด","กรุณาใส่จำนวนเงินที่ถูกต้อง")
        
# funtion การแสดงผลรายการของข้อมูลการขาย
def display_viewlist():
    stat_text ="\n สถิติการขายตั๋ว : \n"
    #อ่านข้อมูลจากไฟล์
    if os.path.exists(DATAFILE):
        with open(DATAFILE ,"r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                stat_text += line #เพิ่มข้อมูลการขายแต่ละบรรทัดลงในข้อความการแสดงผล
    messagebox.showinfo("สถิติการขายตั๋ว",stat_text)

# หน้าจอการแสดง
root = tk.Tk()
root.title("การขายตั๋วรถไฟฟ้าสายสีเขียว สายสุขุมวิท")
root.geometry("800x500")
root.configure(bg="#F0F4C3")

# รายการสถานี
stations = [
    "N24 คูคต","N23 แยก คปอ.","N22 พิพิธภัณฑ์กองทัพอากาศ","N21 โรงพยาบาลภูมิพลอดุยเดช","N20 สะพานใหม่","N19 สายหยุด",
    "N18 พหลโยธิน 59","N17 วัดพระศรีมหาธาตุ","N16 กรมทหารราบที่ 11","N15 บางบัว","N14 กรมป่าไม้","N13 มหาวิทยาลัยเกษตรศาสตร์",
    "N12 เสนานิคม","N11 รัชโยธิน","N10 พหลโยธิน 24","N9 ห้าแยกลาดพร้าว","N8 หมอชิต","N7 สะพานควาย","N5 อารีย์","N4 สนามเป้า",
    "N3 อนุสาวรีย์ชัยสมรภูมิ","N2 พญาไท","N1 ราชเทวี","CEN สยาม","E1 ชิดลม","E2 เพลินจิต","E3 นานา","E4 อโศก","E5 พร้อมพงษ์",
    "E6 ทองหล่อ","E7 เอกมัย","E8 พระโขนง","E9 อ่อนนุช","E10 บางจาก","E11 ปุณณวิถี","E12 อุดมสุข","E13 บางนา","E14 แบริ่ง",
    "E15 สำโรง","E16 ปู่เจ้า","E17 ช้างเอราวัณ","E18 โรงเรียนนายเรือ","E19 ปากน้ำ","E20 ศรีนครินทร์","E21 แพรกษา","E22 สายลวด","E23 เคหะฯ"
]

# เค้าโครง
frame = tk.Frame(root, bg="#C8E6C9")
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# ตั้งค่า grid layout ให้ขยายได้
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_rowconfigure(5, weight=1)
frame.grid_rowconfigure(6, weight=1)



# ชื่อของหน้า
title = tk.Label(frame, text="BTS สายสีเขียว รถไฟฟ้าสายสุขุมวิท", font=("Arial", 24), bg="#388E3C", fg="white")
title.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

# สถานีต้นทาง
tk.Label(frame, text="สถานีต้นทาง", font=("Arial", 14), bg="#A5D6A7", fg="black").grid(row=1, column=0, pady=10, sticky="e")
startStation = ttk.Combobox(frame, values=stations, state="readonly", font=("Arial", 14), width=25,height=10)
startStation.grid(row=1, column=1, pady=5, sticky="w")

# สถานีปลายทาง
tk.Label(frame, text="สถานีปลายทาง", font=("Arial", 14), bg="#A5D6A7", fg="black").grid(row=2, column=0, pady=10, sticky="e")
endStation = ttk.Combobox(frame, values=stations, state="readonly", font=("Arial", 14), width=25,height=10)
endStation.grid(row=2, column=1, pady=5, sticky="w")

#ใส่จำนวนตั๋วที่ต้องการซื้อ
tk.Label(frame,text="จำนวนตั๋วที่ต้องการซื้อ", font=("Arial", 14), bg="#A5D6A7", fg="black").grid(row=3, column=0, pady=10, sticky="e")
ticketCountEntry = tk.Entry(frame,font=("Arial",14),width=30)
ticketCountEntry.grid(row=3,column=1,pady=7,sticky="w")

# ช่องใส่จำนวนเงิน
tk.Label(frame, text="ใส่จำนวนเงิน", font=("Arial", 14), bg="#A5D6A7", fg="black").grid(row=4, column=0, pady=10, sticky="e")
paymentEntry = tk.Entry(frame, font=("Arial", 14), width=30)
paymentEntry.grid(row=4, column=1, pady=7, sticky="w")

# ปุ่มซื้อตั๋ว
btsell = tk.Button(frame, text="ซื้อตั๋ว", command=sellTicket, font=("Arial", 14), bg="#66BB6A", fg="black", width=15, height=2)
btsell.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

# ปุ่มดูประวัติการขายตั๋วรถไฟ 
btviewlist =tk.Button(frame,text="ดูรายการ",command=display_viewlist, font=("Arial", 14), bg="#66BB6A", fg="black", width=15, height=2)
btviewlist.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")

#การแสดงผลลัพธ์
result = tk.Label(frame,text="",bg="#A5D6A7", fg="black")
result.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")
# เพิ่มการผูกฟังก์ชันคำนวณราคาตั๋วกับ Combobox และ Entry
startStation.bind("<<ComboboxSelected>>", lambda event: calculate_ticketprice())
endStation.bind("<<ComboboxSelected>>", lambda event: calculate_ticketprice())
ticketCountEntry.bind("<KeyRelease>", lambda event: calculate_ticketprice())

#สร้าง object ของ คลาส Trainticket_BTS_GreenLine
ticket = Trainticket_BTS_GreenLine()

# เริ่มทำงาน
root.mainloop()
