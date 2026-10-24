import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ClickerGame(ctk.CTk):
    pass
    def __init__(self):
        super().__init__()
        self.title("Клікер гра")
        self.geometry("450x650")
        self.minsize(350, 500)
        self.resizable(True, True)

        self.score = 0
        self.click_power = 1
        self.passive_income = 0
        self.upgrade_click_1_cost = 10
        self.upgrade_click_5_cost = 75
        self.upgrade_passive_1_cost = 50
        self.upgrade_passive_10_cost = 400
        self.multiplier_cost = 1000
        self.score_multiplier = 1

        self.current_font_family = "Arial"
        self.current_btn_color = "#1f6aa5"
        self.current_btn_hover = "#144870"

        self.main_screen = ctk.CTkFrame(self, fg_color="transparent")
        self.main_screen.pack(fill="both", expand=True, padx=20, pady=20)

        self.score_label = ctk.CTkLabel(
            self.main_screen,
            text=f"Рахунок: {self.score}",
            font=ctk.CTkFont(family=self.current_font_family, size=36, weight="bold")
        )
        self.score_label.pack(pady=10)

        self.cps_label = ctk.CTkLabel(
            self.main_screen,
            text="",
            font=ctk.CTkFont(family=self.current_font_family, size=14)
        )
        self.cps_label.pack(pady=5)

        self.click_button = ctk.CTkButton(
            self.main_screen,
            text="КЛІК!",
            width=220,
            height=220,
            corner_radius=110,
            fg_color=self.current_btn_color,
            hover_color=self.current_btn_hover,
            font=ctk.CTkFont(family=self.current_font_family, size=28, weight="bold"),
            command=self.click
        )
        self.click_button.pack(expand=True, pady=20)

        self.bottom_bar = ctk.CTkFrame(self.main_screen, fg_color="transparent")
        self.bottom_bar.pack(side="bottom", fill="x", pady=10)

        self.open_shop_btn = ctk.CTkButton(
            self.bottom_bar,
            text="Магазин 🛒",
            height=50,
            font=ctk.CTkFont(family=self.current_font_family, size=16, weight="bold"),
            command=self.show_shop
        )
        self.open_shop_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.open_settings_btn = ctk.CTkButton(
            self.bottom_bar,
            text="Налаштування ⚙️",
            height=50,
            fg_color="#555555",
            hover_color="#444444",
            font=ctk.CTkFont(family=self.current_font_family, size=16, weight="bold"),
            command=self.show_settings
        )
        self.open_settings_btn.pack(side="right", fill="x", expand=True, padx=(5, 0))

        self.shop_screen = ctk.CTkFrame(self, fg_color="transparent")

        self.shop_title = ctk.CTkLabel(
            self.shop_screen,
            text="Магазин Покращень",
            font=ctk.CTkFont(family=self.current_font_family, size=28, weight="bold")
        )
        self.shop_title.pack(pady=15)

        self.scroll_frame = ctk.CTkScrollableFrame(self.shop_screen, width=380)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.up_click_1_btn = ctk.CTkButton(self.scroll_frame, text="", command=self.buy_click_1)
        self.up_click_1_btn.pack(fill="x", pady=8, ipady=5)

        self.up_click_5_btn = ctk.CTkButton(self.scroll_frame, text="", command=self.buy_click_5)
        self.up_click_5_btn.pack(fill="x", pady=8, ipady=5)

        self.up_pass_1_btn = ctk.CTkButton(self.scroll_frame, text="", command=self.buy_passive_1)
        self.up_pass_1_btn.pack(fill="x", pady=8, ipady=5)

        self.up_pass_10_btn = ctk.CTkButton(self.scroll_frame, text="", command=self.buy_passive_10)
        self.up_pass_10_btn.pack(fill="x", pady=8, ipady=5)

        self.up_mult_btn = ctk.CTkButton(self.scroll_frame, text="", command=self.buy_multiplier)
        self.up_mult_btn.pack(fill="x", pady=8, ipady=5)

        self.close_shop_btn = ctk.CTkButton(
            self.shop_screen,
            text="Назад до гри ↩",
            height=50,
            fg_color="#A12222",
            hover_color="#7A1A1A",
            font=ctk.CTkFont(family=self.current_font_family, size=16, weight="bold"),
            command=self.show_main
        )
        self.close_shop_btn.pack(side="bottom", fill="x", pady=10)

        self.settings_screen = ctk.CTkFrame(self, fg_color="transparent")

        self.settings_title = ctk.CTkLabel(
            self.settings_screen,
            text="Налаштування",
            font=ctk.CTkFont(family=self.current_font_family, size=28, weight="bold")
        )
        self.settings_title.pack(pady=15)

        self.font_label = ctk.CTkLabel(
            self.settings_screen,
            text="Оберіть шрифт інтерфейсу:",
            font=ctk.CTkFont(family=self.current_font_family, size=16)
        )
        self.font_label.pack(pady=(20, 5))

        self.font_menu = ctk.CTkOptionMenu(
            self.settings_screen,
            values=["Arial", "Times New Roman", "Courier New", "Comic Sans MS"],
            command=self.change_font
        )
        self.font_menu.set(self.current_font_family)
        self.font_menu.pack(pady=5)

        self.color_label = ctk.CTkLabel(
            self.settings_screen,
            text="Колір кнопки кліку:",
            font=ctk.CTkFont(family=self.current_font_family, size=16)
        )
        self.color_label.pack(pady=(20, 5))

        self.color_menu = ctk.CTkOptionMenu(
            self.settings_screen,
            values=["Синій", "Зелений", "Пурпурний", "Помаранчевий"],
            command=self.change_button_color
        )
        self.color_menu.set("Синій")
        self.color_menu.pack(pady=5)

        self.close_settings_btn = ctk.CTkButton(
            self.settings_screen,
            text="Назад до гри ↩",
            height=50,
            fg_color="#A12222",
            hover_color="#7A1A1A",
            font=ctk.CTkFont(family=self.current_font_family, size=16, weight="bold"),
            command=self.show_main
        )
        self.close_settings_btn.pack(side="bottom", fill="x", pady=10)

        self.update_ui()
        self.run_passive_income()
        self.bind("<Configure>", self.ui_adaptive)

    def click(self):
        self.score += self.click_power * self.score_multiplier
        self.update_ui()

    def show_shop(self):
        self.main_screen.pack_forget()
        self.settings_screen.pack_forget()
        self.shop_screen.pack(fill="both", expand=True, padx=20, pady=20)
        self.update_ui()

    def show_settings(self):
        self.main_screen.pack_forget()
        self.shop_screen.pack_forget()
        self.settings_screen.pack(fill="both", expand=True, padx=20, pady=20)
        self.update_ui()

    def show_main(self):
        self.shop_screen.pack_forget()
        self.settings_screen.pack_forget()
        self.main_screen.pack(fill="both", expand=True, padx=20, pady=20)
        self.update_ui()

    def change_font(self, chosen_font):
        self.current_font_family = chosen_font
        self.ui_adaptive()

    def change_button_color(self, chosen_color):
        color_map = {
            "Синій": ("#1f6aa5", "#144870"),
            "Зелений": ("#2ed573", "#26af5f"),
            "Пурпурний": ("#9b59b6", "#8e44ad"),
            "Помаранчевий": ("#e67e22", "#d35400")
        }
        self.current_btn_color, self.current_btn_hover = color_map.get(chosen_color, ("#1f6aa5", "#144870"))
        self.click_button.configure(fg_color=self.current_btn_color, hover_color=self.current_btn_hover)

    def buy_click_1(self):
        if self.score >= self.upgrade_click_1_cost:
            self.score -= self.upgrade_click_1_cost
            self.click_power += 1
            self.upgrade_click_1_cost = int(self.upgrade_click_1_cost * 1.4)
            self.update_ui()

    def buy_click_5(self):
        if self.score >= self.upgrade_click_5_cost:
            self.score -= self.upgrade_click_5_cost
            self.click_power += 5
            self.upgrade_click_5_cost = int(self.upgrade_click_5_cost * 1.5)
            self.update_ui()

    def buy_passive_1(self):
        if self.score >= self.upgrade_passive_1_cost:
            self.score -= self.upgrade_passive_1_cost
            self.passive_income += 1
            self.upgrade_passive_1_cost = int(self.upgrade_passive_1_cost * 1.4)
            self.update_ui()

    def buy_passive_10(self):
        if self.score >= self.upgrade_passive_10_cost:
            self.score -= self.upgrade_passive_10_cost
            self.passive_income += 10
            self.upgrade_passive_10_cost = int(self.upgrade_passive_10_cost * 1.5)
            self.update_ui()

    def buy_multiplier(self):
        if self.score >= self.multiplier_cost:
            self.score -= self.multiplier_cost
            self.score_multiplier *= 2
            self.multiplier_cost = int(self.multiplier_cost * 3.5)
            self.update_ui()

    def update_ui(self):
        self.score_label.configure(text=f"Рахунок: {self.score}")
        self.cps_label.configure(
            text=f"Дохід за клік: +{self.click_power * self.score_multiplier}\nПасивний дохід: +{self.passive_income * self.score_multiplier}/сек\nМультиплікатор: x{self.score_multiplier}"
        )
        self.up_click_1_btn.configure(text=f"Легкий клік (+1 до кліку)\nЦіна: {self.upgrade_click_1_cost}")
        self.up_click_5_btn.configure(text=f"Мега клік (+5 до кліку)\nЦіна: {self.upgrade_click_5_cost}")
        self.up_pass_1_btn.configure(text=f"Автоклікер (+1/сек)\nЦіна: {self.upgrade_passive_1_cost}")
        self.up_pass_10_btn.configure(text=f"Ферма кліків (+10/сек)\nЦіна: {self.upgrade_passive_10_cost}")
        self.up_mult_btn.configure(text=f"Множник рахунку (x2 до всього)\nЦіна: {self.multiplier_cost}")
        self.up_mult_btn.configure(text=f"Множник рахунку (x2 до всього)\nЦіна: {self.multiplier_cost}")

    def run_passive_income(self):
        if self.passive_income > 0:
            self.score += self.passive_income * self.score_multiplier
            self.score_label.configure(text=f"Рахунок: {self.score}")
        self.after(1000, self.run_passive_income)

    def ui_adaptive(self, event=None):
        width = self.winfo_width()
        height = self.winfo_height()
        scale = min(width / 450, height / 650)
        btn_size = int(max(140, min(300, 220 * scale)))

        self.click_button.configure(
            width=btn_size,
            height=btn_size,
            corner_radius=btn_size // 2,
            font=ctk.CTkFont(family=self.current_font_family, size=int(max(18, 28 * scale)), weight="bold")
        )
        self.score_label.configure(
            font=ctk.CTkFont(family=self.current_font_family, size=int(max(24, 36 * scale)), weight="bold"))
        self.cps_label.configure(font=ctk.CTkFont(family=self.current_font_family, size=int(max(11, 14 * scale))))
        self.shop_title.configure(
            font=ctk.CTkFont(family=self.current_font_family, size=int(max(20, 28 * scale)), weight="bold"))
        self.settings_title.configure(
            font=ctk.CTkFont(family=self.current_font_family, size=int(max(20, 28 * scale)), weight="bold"))
        self.font_label.configure(font=ctk.CTkFont(family=self.current_font_family, size=int(max(13, 16 * scale))))
        self.color_label.configure(font=ctk.CTkFont(family=self.current_font_family, size=int(max(13, 16 * scale))))

        button_font = ctk.CTkFont(family=self.current_font_family, size=int(max(12, 16 * scale)), weight="bold")
        self.open_shop_btn.configure(font=button_font)
        self.open_settings_btn.configure(font=button_font)
        self.close_shop_btn.configure(font=button_font)
        self.close_settings_btn.configure(font=button_font)

        shop_btn_font = ctk.CTkFont(family=self.current_font_family, size=int(max(11, 14 * scale)))
        self.up_click_1_btn.configure(font=shop_btn_font)
        self.up_click_5_btn.configure(font=shop_btn_font)
        self.up_pass_1_btn.configure(font=shop_btn_font)
        self.up_pass_10_btn.configure(font=shop_btn_font)
        self.up_mult_btn.configure(font=shop_btn_font)


if __name__ == "__main__":
    app = ClickerGame()
    app.mainloop()