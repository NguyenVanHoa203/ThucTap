contacts = {}

def add_contact():
    name = input("Tên: ")
    phone = input("Số điện thoại: ")
    contacts[name] = phone
    print("Đã thêm.")

def view_contacts():
    print("Danh bạ:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact():
    name = input("Nhập tên để tìm: ")
    phone = contacts.get(name)
    if phone:
        print(f"{name}: {phone}")
    else:
        print("❌ Không tìm thấy.")

def delete_contact():
    name = input("Nhập tên để xóa: ")
    if name in contacts:
        del contacts[name]
        print("Đã xóa.")
    else:
        print("Không có trong danh bạ.")

def contact_book():
    while True:
        print("\n1. Thêm\n2. Xem\n3. Tìm\n4. Xóa\n5. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Tạm biệt!")
            break
        else:
            print("Chọn sai.")

contact_book()
