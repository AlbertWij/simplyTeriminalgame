import random
import sys
import time
from collections import deque

class Menu:
    def menu_awal(self):
        while True:
            print("< Simple leveling RPG >")
            mulai = input("Mulai Game? (Y/N)\t")
            if mulai.lower() == "y":
                break
            elif mulai.lower() == "n":
                print("Game dihentikan.")
                sys.exit()
            else:
                print("Tidak Diketahui, silakan masukkan Y atau N")

    def menu_loading(self, duration):
        tools = ['|', '/', '-', '\\']
        start_time = time.time()

        while (time.time() - start_time) < duration:
            for symbol in tools:
                sys.stdout.write('\r' + 'Loading... ' + symbol)
                sys.stdout.flush()
                time.sleep(0.2)
        sys.stdout.write('\r' + 'Loading... Selesai!\n')

    def menu_akhir(self):
        ulang = input("Apakah Ingin Mengulang Lagi? (Y/N)\t")
        if ulang.lower() == "y":
            return self.menu_awal()
        elif ulang.lower() == "n":
            print("Game dihentikan.")
            sys.exit()
        else:
            print("Tidak Diketahui, silakan masukkan Y atau N")

    def menu_kalah(self):
        print("Anda Kalah! Silahkan Coba Lagi!")
        return self.menu_akhir()

    def menu_tamat(self):
        print("Selamat! Anda telah menyelesaikan permainan.")
        return self.menu_akhir()

class Character:
    def __init__(self):
        self.hp = 0
        self.total_att = 0
        self.mana = 0
        self.char_name = ""

    def ninja(self):
        self.hp = 100
        self.total_att = 30
        self.mana = 30
        self.char_name = "Ninja 🗡"
        return self.char_name

    def swordman(self):
        self.hp = 250
        self.total_att = 20
        self.mana = 30
        self.char_name = "Swordman ⚔"
        return self.char_name

    def sorcerer(self):
        self.hp = 150
        self.total_att = 25
        self.mana = 30
        self.char_name = "Sorcerer ⚕"
        return self.char_name

    def tank(self):
        self.hp = 400
        self.total_att = 20
        self.mana = 50
        self.char_name = "Tank 🛡"
        return self.char_name

    def pick(self, pick_char):
        if pick_char.lower() == "ninja":
            return self.ninja()
        elif pick_char.lower() == "swordman":
            return self.swordman()
        elif pick_char.lower() == "sorcerer":
            return self.sorcerer()
        elif pick_char.lower() == "tank":
            return self.tank()
        else:
            print("Role Tidak Diketahui.")
            return menu.menu_awal()

    def status(self):
        return f"HP: {self.hp}\nTotal Attack: {self.total_att}\nMana: {self.mana}"

class Enemies:
    def __init__(self):
        self.hp = 0
        self.total_att = 0
        self.enemy_name = ""

    def elf(self):
        self.hp = 70
        self.total_att = 30
        self.enemy_name = "Elf"
        return self

    def orc(self):
        self.hp = 80
        self.total_att = 30
        self.enemy_name = "Orc"
        return self

    def skeleton(self):
        self.hp = 90
        self.total_att = 30
        self.enemy_name = "Skeleton"
        return self

    def titan(self):
        self.hp = 100
        self.total_att = 20
        self.enemy_name = "Titan"
        return self

class Items:
    def __init__(self):
        self.items = {
            "superPotion": {"attMultiplier": 2},
            "manaPotion": {"manaRecover": 20},
            "attPotion": {"attPlus": 20}
        }

    def use_item(self, item_name, character):
        if item_name.lower() == "superpotion":
            character.total_att *= self.items["superPotion"]["attMultiplier"]
        elif item_name.lower() == "manapotion":
            character.mana += self.items["manaPotion"]["manaRecover"]
        elif item_name.lower() == "attpotion":
            character.total_att += self.items["attPotion"]["attPlus"]

class Backpack:
    def __init__(self):
        self.stack = []
        self.item_count = 0

    def is_empty_stack(self):
        return len(self.stack) == 0

    def push(self, item):
        self.item_count += 1
        item_with_count = f"{item}{self.item_count}"
        self.stack.append(item_with_count)

    def pop(self):
        if not self.is_empty_stack():
            item_with_count = self.stack.pop()
            return item_with_count
        else:
            return "Backpack Kosong!."

    def show_items(self):
        return f"Stack: {self.stack}"

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return "Queue Kosong!."

    def show_items(self):
        return f"Queue: {list(self.queue)}"

class Gameplay:
    def __init__(self):
        self.current_enemy = None

    def attack(self, character, enemy):
        damage = character.total_att
        enemy.hp -= damage
        if enemy.hp <= 0:
            print(f"{enemy.enemy_name} dikalahkan!")
            return "Menang!"
        return f"Menyerang {enemy.enemy_name} dengan {damage} damage."

    def skill(self, character, enemy):
        if character.mana >= 10:
            character.mana -= 10
            damage = character.total_att * 2
            enemy.hp -= damage
            if enemy.hp <= 0:
                print(f"{enemy.enemy_name} dikalahkan!")
                return "Menang!"
            return f"Menggunakan Skill pada {enemy.enemy_name} untuk {damage} damage."
        else:
            return "Mana tidak cukup!."

    def use_items(self, backpack, queue, character, item_name):
        if backpack.is_empty_stack():
            print("Backpack kosong!")
            return

        item = backpack.pop()
        queue.enqueue(item)
        if item.lower().startswith(item_name.lower()):
            items = Items()
            items.use_item(item_name, character)
            print(f"Menggunakan {item} pada {character.char_name}.")
            queue.dequeue()
        else:
            print(f"{item_name} tidak tersedia di Backpack! Ambil item pertama yang berlaku: {item}")
            backpack.push(item)
            queue.dequeue()

    def respawn_enemy(self):
        enemy = Enemies()
        enemies_methods = [enemy.elf, enemy.orc, enemy.skeleton, enemy.titan]
        self.current_enemy = random.choice(enemies_methods)()

    def story(self):
        stories = [
            "Memasuki Hutan, terdapat 3 pohon besar menghalangi, berjalan memutar.",
            "Mulai menaiki Gunung. Jalanan curam dan terjang.",
            "Melewati Sungai. Terdapat air terjun besar.",
            "Singgah di kota yang penuh penjahat kelas atas.",
            "Berhasil melarikan diri. Terus berjalan.",
            "Bertemu dengan pertapa tua.",
            "Bertemu dengan Naga Legendaris.",
            "Memasuki kawasan berkabut.",
            "Menolong seseorang misterius.",
            "Berhasil melarikan diri. Memasuki wilayah Orc."
        ]
        for story in stories:
            print(story)
            time.sleep(3)
            self.respawn_enemy()
            print(f"Berhadapan dengan musuh: {self.current_enemy.enemy_name}")

            while self.current_enemy.hp > 0:
                action = input("Pilih aksi (attack/skill/item): ")
                if action.lower() == "attack":
                    result = self.attack(char, self.current_enemy)
                    print(result)
                elif action.lower() == "skill":
                    result = self.skill(char, self.current_enemy)
                    print(result)
                elif action.lower() == "item":
                    print(backpack.show_items())
                    item = input("Masukan nama item yang dipakai: ")
                    self.use_items(backpack, queue, char, item)
                    print(char.status())
                else:
                    print("Aksi tidak diketahui.")

            if self.current_enemy.hp <= 0:
                print("Melanjutkan ke cerita berikutnya...")
            else:
                return menu.menu_kalah()

            yield random.choice(["superPotion", "manaPotion", "attPotion"])

# Main Program
menu = Menu()
char = Character()
backpack = Backpack()
queue = Queue()
gameplay = Gameplay()
items = Items()

menu.menu_loading(2)
print()
menu.menu_awal()
print()
menu.menu_loading(3)

print("< Keterangan Game >")
print("- Pilih Karakter yang Di inginkan.\n- Terdapat 2 Macam Interaksi Karakter, yaitu Attack dan Skill.\n- Status Attack Awal akan Diperlihatkan dan akan Menyesuaikan Setelah Mendapat Item Bonus.\n- Kekuatan Skill Merupakan 2x dari Total Attack.\n- Menggunakan skill mengurangi mana sebesar 10.")
print()
print("< Pilih Role >")
pick_char = input("- Ninja\n- Swordman\n- Sorcerer\n- Tank\nRole\t\t: ")

menu.menu_loading(3)

terpilih = char.pick(pick_char)
if terpilih != "Role Tidak Diketahui.":
    print("\n\nSelamat Berpetualang sebagai", terpilih)
    print("\nBerikut Status Karakter :\n")
    print(char.status())
else:
    print("Role Tidak Diketahui.")
    sys.exit()

print()
menu.menu_loading(2)
print()

story_gen = gameplay.story()
for item in story_gen:
    print(f"Item ditemukan: {item}")
    backpack.push(item)
    print(backpack.show_items())
    time.sleep(2)

enemy = Enemies().elf()
print(f"Berhadapan dengan musuh: {enemy.enemy_name}")

while enemy.hp > 0:
    action = input("Pilih aksi (attack/skill/item): ")
    if action.lower() == "attack":
        result = gameplay.attack(char, enemy)
        print(result)
    elif action.lower() == "skill":
        result = gameplay.skill(char, enemy)
        print(result)
    elif action.lower() == "item":
        print(backpack.show_items())
        item = input("Masukan nama item yang dipakai: ")
        gameplay.use_items(backpack, queue, char, item)
        print(char.status())
    else:
        print("Aksi tidak diketahui.")

if enemy.hp <= 0:
    menu.menu_tamat()
else:
    menu.menu_kalah()
