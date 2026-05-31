import tkinter as tk
from tkinter import ttk, messagebox
import math


# ── helpers ──────────────────────────────────────────────────────────────────

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq

def is_perfect_square(n):
    s = int(math.isqrt(n))
    return s * s == n

def is_fibonacci_num(n):
    if n < 0:
        return False
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def get_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_even(seq):
    return [x for x in seq if x % 2 == 0]

def fibonacci_odd(seq):
    return [x for x in seq if x % 2 != 0]


# ── main app ─────────────────────────────────────────────────────────────────

class FibonacciApp(tk.Tk):

    BG     = "#0f0f1a"
    PANEL  = "#1a1a2e"
    CARD   = "#16213e"
    ACCENT = "#e94560"
    ACC2   = "#0f3460"
    TEXT   = "#eaeaea"
    MUTED  = "#8888aa"
    GREEN  = "#00d4aa"
    YELLOW = "#f5a623"
    BORDER = "#2a2a4a"
    FONT   = "Segoe UI"

    def __init__(self):
        super().__init__()
        self.title("Fibonacci Generator — Hex Softwares")
        self.geometry("1000x700")
        self.minsize(900, 620)
        self.configure(bg=self.BG)
        self._build_ui()
        self._animate_title()

    # ── UI skeleton ──────────────────────────────────────────────────────────

    def _build_ui(self):
        # sidebar
        sidebar = tk.Frame(self, bg=self.PANEL, width=230)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="⟨F⟩", font=(self.FONT, 30, "bold"),
                 bg=self.PANEL, fg=self.ACCENT).pack(pady=(28, 2))
        tk.Label(sidebar, text="FIBONACCI GENERATOR",
                 font=(self.FONT, 9, "bold"), bg=self.PANEL, fg=self.TEXT).pack()
        tk.Label(sidebar, text="Hex Softwares Internship",
                 font=(self.FONT, 8), bg=self.PANEL, fg=self.MUTED).pack()

        tk.Frame(sidebar, bg=self.BORDER, height=1).pack(fill="x", padx=18, pady=18)

        self.nav_btns = {}
        tabs = [
            ("🔢", "Generate Series",  "generate"),
            ("🔍", "Check Number",     "check"),
            ("📍", "Nth Term",         "nth"),
            ("📊", "Statistics",       "stats"),
            ("🔄", "Reverse Series",   "reverse"),
            ("📈", "Visualizer",       "visual"),
            ("ℹ️",  "About",            "about"),
        ]
        for icon, label, key in tabs:
            btn = tk.Button(sidebar,
                text=f"   {icon}  {label}",
                font=(self.FONT, 10), anchor="w",
                bg=self.PANEL, fg=self.MUTED,
                activebackground=self.ACC2, activeforeground=self.TEXT,
                bd=0, padx=10, pady=10, cursor="hand2",
                command=lambda k=key: self._show_tab(k))
            btn.pack(fill="x", padx=6, pady=1)
            self.nav_btns[key] = btn

        tk.Label(sidebar, text="© 2025 Hex Softwares",
                 font=(self.FONT, 8), bg=self.PANEL,
                 fg=self.MUTED).pack(side="bottom", pady=12)

        # main
        main = tk.Frame(self, bg=self.BG)
        main.pack(side="left", fill="both", expand=True)

        hdr = tk.Frame(main, bg=self.PANEL, height=58)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        self.hdr_title = tk.Label(hdr, text="",
                                  font=(self.FONT, 15, "bold"),
                                  bg=self.PANEL, fg=self.TEXT)
        self.hdr_title.pack(side="left", padx=22, pady=14)
        self.hdr_sub = tk.Label(hdr, text="",
                                font=(self.FONT, 9),
                                bg=self.PANEL, fg=self.MUTED)
        self.hdr_sub.pack(side="left")

        container = tk.Frame(main, bg=self.BG)
        container.pack(fill="both", expand=True, padx=22, pady=18)

        self.pages = {}
        for key in ["generate","check","nth","stats","reverse","visual","about"]:
            pg = tk.Frame(container, bg=self.BG)
            pg.place(relwidth=1, relheight=1)
            self.pages[key] = pg

        self._build_generate()
        self._build_check()
        self._build_nth()
        self._build_stats()
        self._build_reverse()
        self._build_visual()
        self._build_about()
        self._show_tab("generate")

    # ── navigation ───────────────────────────────────────────────────────────

    def _show_tab(self, key):
        labels = {
            "generate": ("Generate Fibonacci Series",  "First N numbers of the sequence"),
            "check":    ("Check a Number",              "Is it a Fibonacci number?"),
            "nth":      ("Find the Nth Term",           "0-indexed position lookup"),
            "stats":    ("Series Statistics",           "Sum, average, even/odd breakdown"),
            "reverse":  ("Reverse Series",              "Descending Fibonacci order"),
            "visual":   ("Bar Visualizer",              "Visual bar chart of the series"),
            "about":    ("About",                       "Hex Softwares Internship — Task 1"),
        }
        for k, b in self.nav_btns.items():
            active = (k == key)
            b.config(bg=self.ACC2 if active else self.PANEL,
                     fg=self.TEXT if active else self.MUTED,
                     font=(self.FONT, 10, "bold") if active else (self.FONT, 10))
        self.pages[key].lift()
        t, s = labels[key]
        self.hdr_title.config(text=t)
        self.hdr_sub.config(text=f"  —  {s}")

    # ── shared helpers ────────────────────────────────────────────────────────

    def _card(self, parent, title="", pady=8):
        f = tk.Frame(parent, bg=self.CARD,
                     highlightbackground=self.BORDER, highlightthickness=1)
        f.pack(fill="x", pady=pady)
        if title:
            tk.Label(f, text=title, font=(self.FONT, 10, "bold"),
                     bg=self.CARD, fg=self.ACCENT).pack(anchor="w", padx=16, pady=(12,4))
        inner = tk.Frame(f, bg=self.CARD)
        inner.pack(fill="both", padx=16, pady=(0,14))
        return inner

    def _entry(self, parent, ph="", w=14):
        e = tk.Entry(parent, font=(self.FONT, 12),
                     bg=self.ACC2, fg=self.TEXT,
                     insertbackground=self.TEXT,
                     relief="flat", bd=0, width=w)
        e.insert(0, ph)
        e.bind("<FocusIn>",  lambda ev, _e=e, _p=ph: _e.delete(0,"end") if _e.get()==_p else None)
        e.bind("<FocusOut>", lambda ev, _e=e, _p=ph: _e.insert(0,_p)   if _e.get()==""  else None)
        return e

    def _btn(self, parent, text, cmd, color=None):
        return tk.Button(parent, text=text,
                         font=(self.FONT, 10, "bold"),
                         bg=color or self.ACCENT, fg="white",
                         relief="flat", bd=0,
                         padx=18, pady=7, cursor="hand2",
                         command=cmd,
                         activebackground=self.MUTED,
                         activeforeground="white")

    def _result_box(self, parent, height=7):
        f = tk.Frame(parent, bg=self.CARD,
                     highlightbackground=self.BORDER, highlightthickness=1)
        f.pack(fill="both", expand=True, pady=(10,0))
        tk.Label(f, text="Result", font=(self.FONT, 8, "bold"),
                 bg=self.CARD, fg=self.MUTED).pack(anchor="w", padx=14, pady=(8,2))
        txt = tk.Text(f, font=(self.FONT, 11),
                      bg=self.BG, fg=self.GREEN,
                      relief="flat", bd=0, height=height,
                      wrap="word", state="disabled",
                      padx=14, pady=8)
        sb = ttk.Scrollbar(f, orient="vertical", command=txt.yview)
        txt.config(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        txt.pack(fill="both", expand=True, padx=(8,0), pady=(0,8))
        return txt

    def _write(self, w, text, color=None):
        w.config(state="normal")
        w.delete("1.0","end")
        w.insert("end", text)
        if color:
            w.config(fg=color)
        w.config(state="disabled")

    def _copy(self, w):
        txt = w.get("1.0","end").strip()
        if txt:
            self.clipboard_clear()
            self.clipboard_append(txt)
            messagebox.showinfo("Copied ✔", "Result copied to clipboard!")

    def _pill(self, parent, label, value):
        f = tk.Frame(parent, bg=self.CARD,
                     highlightbackground=self.BORDER, highlightthickness=1)
        f.pack(side="left", padx=(0,8), pady=4, ipadx=14, ipady=6)
        tk.Label(f, text=label, font=(self.FONT, 8),
                 bg=self.CARD, fg=self.MUTED).pack()
        v = tk.Label(f, text=value, font=(self.FONT, 13, "bold"),
                     bg=self.CARD, fg=self.ACCENT)
        v.pack()
        return v

    # ── PAGE: Generate ───────────────────────────────────────────────────────

    def _build_generate(self):
        p = self.pages["generate"]
        c = self._card(p, "🔢  Enter how many Fibonacci numbers to generate")
        row = tk.Frame(c, bg=self.CARD); row.pack(fill="x")
        self.gen_entry = self._entry(row, "e.g.  15")
        self.gen_entry.pack(side="left", ipady=6, padx=(0,10))
        self._btn(row, "Generate", self._do_generate).pack(side="left")
        self._btn(row, "Clear", lambda: [
            self._write(self.gen_out, ""),
            self.p_count.config(text="—"),
            self.p_sum.config(text="—"),
            self.p_last.config(text="—"),
            self.p_even.config(text="—"),
        ], self.MUTED).pack(side="left", padx=(8,0))

        pills = tk.Frame(p, bg=self.BG); pills.pack(fill="x", pady=(6,0))
        self.p_count = self._pill(pills, "Count", "—")
        self.p_sum   = self._pill(pills, "Sum",   "—")
        self.p_last  = self._pill(pills, "Largest","—")
        self.p_even  = self._pill(pills, "Even #s","—")

        self.gen_out = self._result_box(p, height=9)
        self._btn(p, "📋  Copy Result", lambda: self._copy(self.gen_out), self.ACC2).pack(anchor="w", pady=(8,0))

    def _do_generate(self):
        try:
            n = int(self.gen_entry.get())
            if n <= 0: raise ValueError
            seq = generate_fibonacci(n)
            self.p_count.config(text=str(len(seq)))
            self.p_sum.config(text=f"{sum(seq):,}")
            self.p_last.config(text=f"{seq[-1]:,}")
            self.p_even.config(text=str(len(fibonacci_even(seq))))
            lines = [f"  [{i:>4}]   {v:,}" for i,v in enumerate(seq)]
            self._write(self.gen_out, "\n".join(lines), self.GREEN)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer.")

    # ── PAGE: Check ──────────────────────────────────────────────────────────

    def _build_check(self):
        p = self.pages["check"]
        c = self._card(p, "🔍  Enter any number to check")
        row = tk.Frame(c, bg=self.CARD); row.pack(fill="x")
        self.chk_entry = self._entry(row, "e.g.  144")
        self.chk_entry.pack(side="left", ipady=6, padx=(0,10))
        self._btn(row, "Check", self._do_check).pack(side="left")
        self.chk_out = self._result_box(p, height=7)

    def _do_check(self):
        try:
            n = int(self.chk_entry.get())
            yes = is_fibonacci_num(n)
            if yes:
                idx = self._find_index(n)
                msg = (f"  ✔   {n:,} IS a Fibonacci number!\n\n"
                       f"  Position in sequence  :  {idx}\n"
                       f"  Previous Fibonacci    :  {self._nearest_fib(n)[0]:,}\n"
                       f"  Next Fibonacci        :  {self._nearest_fib(n)[1]:,}")
                self._write(self.chk_out, msg, self.GREEN)
            else:
                lo, hi = self._nearest_fib(n)
                msg = (f"  ✘   {n:,} is NOT a Fibonacci number.\n\n"
                       f"  Nearest lower Fibonacci  :  {lo:,}\n"
                       f"  Nearest upper Fibonacci  :  {hi:,}")
                self._write(self.chk_out, msg, self.ACCENT)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def _find_index(self, n):
        a, b, i = 0, 1, 0
        while a < n:
            a, b = b, a+b; i += 1
        return i

    def _nearest_fib(self, n):
        a, b = 0, 1
        while b < n:
            a, b = b, a+b
        return a, b

    # ── PAGE: Nth ────────────────────────────────────────────────────────────

    def _build_nth(self):
        p = self.pages["nth"]
        c = self._card(p, "📍  Enter position (0-indexed)")
        row = tk.Frame(c, bg=self.CARD); row.pack(fill="x")
        self.nth_entry = self._entry(row, "e.g.  10")
        self.nth_entry.pack(side="left", ipady=6, padx=(0,10))
        self._btn(row, "Find", self._do_nth).pack(side="left")
        self.nth_out = self._result_box(p, height=6)

    def _do_nth(self):
        try:
            n = int(self.nth_entry.get())
            if n < 0: raise ValueError
            val = get_nth_fibonacci(n)
            prev = get_nth_fibonacci(n-1) if n > 0 else "—"
            nxt  = get_nth_fibonacci(n+1)
            msg = (f"  Position     :  {n}\n"
                   f"  F({n})        :  {val:,}\n\n"
                   f"  Previous     :  F({n-1}) = {prev:,}" if isinstance(prev,int) else
                   f"  Previous     :  —"
                   f"\n  Next         :  F({n+1}) = {nxt:,}")
            self._write(self.nth_out, msg, self.YELLOW)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid non-negative integer.")

    # ── PAGE: Stats ──────────────────────────────────────────────────────────

    def _build_stats(self):
        p = self.pages["stats"]
        c = self._card(p, "📊  Analyze first N Fibonacci numbers")
        row = tk.Frame(c, bg=self.CARD); row.pack(fill="x")
        self.stat_entry = self._entry(row, "e.g.  20")
        self.stat_entry.pack(side="left", ipady=6, padx=(0,10))
        self._btn(row, "Analyze", self._do_stats).pack(side="left")
        self.stat_out = self._result_box(p, height=13)

    def _do_stats(self):
        try:
            n = int(self.stat_entry.get())
            if n <= 0: raise ValueError
            seq   = generate_fibonacci(n)
            evens = fibonacci_even(seq)
            odds  = fibonacci_odd(seq)
            total = sum(seq)
            avg   = total / n
            ratio = f"{seq[-1]/seq[-2]:.10f}" if n >= 2 else "N/A"
            lines = [
                f"  📌  Count              :  {n}",
                f"  ➕  Total Sum          :  {total:,}",
                f"  📐  Average            :  {avg:,.4f}",
                f"  🔼  Largest            :  {seq[-1]:,}",
                f"  🔽  Smallest           :  {seq[0]:,}",
                f"  📏  Golden Ratio (last two terms)  :  {ratio}",
                f"",
                f"  ✅  Even numbers  ({len(evens)}) :",
                f"      {', '.join(map(str, evens)) or 'None'}",
                f"",
                f"  🔵  Odd numbers   ({len(odds)}) :",
                f"      {', '.join(map(str, odds[:30]))}{'...' if len(odds)>30 else ''}",
            ]
            self._write(self.stat_out, "\n".join(lines), self.YELLOW)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer.")

    # ── PAGE: Reverse ────────────────────────────────────────────────────────

    def _build_reverse(self):
        p = self.pages["reverse"]
        c = self._card(p, "🔄  Reverse Fibonacci Series")
        row = tk.Frame(c, bg=self.CARD); row.pack(fill="x")
        self.rev_entry = self._entry(row, "e.g.  10")
        self.rev_entry.pack(side="left", ipady=6, padx=(0,10))
        self._btn(row, "Reverse", self._do_reverse).pack(side="left")
        self.rev_out = self._result_box(p, height=9)
        self._btn(p, "📋  Copy Result", lambda: self._copy(self.rev_out), self.ACC2).pack(anchor="w", pady=(8,0))

    def _do_reverse(self):
        try:
            n = int(self.rev_entry.get())
            if n <= 0: raise ValueError
            seq = list(reversed(generate_fibonacci(n)))
            lines = [f"  [{i:>4}]   {v:,}" for i,v in enumerate(seq)]
            self._write(self.rev_out, "\n".join(lines), self.GREEN)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer.")

    # ── PAGE: Visualizer ─────────────────────────────────────────────────────

    def _build_visual(self):
        p = self.pages["visual"]
        c = self._card(p, "📈  Bar Chart — enter count (2–25 recommended)")
        row = tk.Frame(c, bg=self.CARD); row.pack(fill="x")
        self.vis_entry = self._entry(row, "e.g.  12")
        self.vis_entry.pack(side="left", ipady=6, padx=(0,10))
        self._btn(row, "Visualize", self._do_visual).pack(side="left")

        cf = tk.Frame(p, bg=self.CARD,
                      highlightbackground=self.BORDER, highlightthickness=1)
        cf.pack(fill="both", expand=True, pady=(12,0))
        self.vis_canvas = tk.Canvas(cf, bg=self.BG, highlightthickness=0)
        self.vis_canvas.pack(fill="both", expand=True, padx=10, pady=10)

    def _do_visual(self):
        try:
            n = int(self.vis_entry.get())
            if n < 2:
                messagebox.showwarning("Range", "Enter at least 2.")
                return
            self._draw_bars(generate_fibonacci(min(n, 30)))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer.")

    def _draw_bars(self, seq):
        c = self.vis_canvas
        c.delete("all")
        c.update_idletasks()
        W, H = c.winfo_width(), c.winfo_height()
        pl, pr, pt, pb = 55, 20, 20, 45
        n = len(seq)
        mx = max(seq) or 1
        bw = (W - pl - pr) / n
        colors = ["#e94560","#0f3460","#00d4aa","#f5a623",
                  "#a855f7","#06b6d4","#84cc16","#f43f5e"]
        for i, val in enumerate(seq):
            x0 = pl + i*bw + bw*0.1
            x1 = pl + (i+1)*bw - bw*0.1
            bh = (val/mx)*(H-pt-pb)
            y0 = H - pb - bh
            y1 = H - pb
            col = colors[i % len(colors)]
            c.create_rectangle(x0, y0, x1, y1, fill=col, outline="", width=0)
            if bw > 26:
                c.create_text((x0+x1)/2, y0-7, text=f"{val:,}",
                              fill=self.TEXT, font=(self.FONT, 8))
            c.create_text((x0+x1)/2, H-pb+14, text=str(i),
                          fill=self.MUTED, font=(self.FONT, 8))
        c.create_line(pl, pt, pl, H-pb, fill=self.BORDER, width=1)
        c.create_line(pl, H-pb, W-pr, H-pb, fill=self.BORDER, width=1)
        # y labels
        for step in [0.25, 0.5, 0.75, 1.0]:
            y = H - pb - step*(H-pt-pb)
            val = int(mx*step)
            c.create_line(pl-4, y, pl, y, fill=self.MUTED, width=1)
            c.create_text(pl-6, y, text=f"{val:,}",
                          fill=self.MUTED, font=(self.FONT, 7), anchor="e")

    # ── PAGE: About ──────────────────────────────────────────────────────────

    def _build_about(self):
        p = self.pages["about"]
        c = self._card(p)
        tk.Label(c, text="⟨F⟩", font=(self.FONT, 44, "bold"),
                 bg=self.CARD, fg=self.ACCENT).pack(pady=(12,4))
        tk.Label(c, text="Fibonacci Generator",
                 font=(self.FONT, 20, "bold"), bg=self.CARD, fg=self.TEXT).pack()
        tk.Label(c, text="Hex Softwares  ·  Python Internship  ·  Task 1",
                 font=(self.FONT, 10), bg=self.CARD, fg=self.MUTED).pack(pady=(4,18))
        info = [
            ("Language",  "Python 3  —  built-in libraries only (tkinter, math)"),
            ("Features",  "Generate · Check · Nth Term · Stats · Reverse · Visualizer"),
            ("GUI",       "Tkinter  —  dark theme, sidebar navigation"),
            ("Series",    "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ..."),
        ]
        for k, v in info:
            row = tk.Frame(c, bg=self.CARD); row.pack(fill="x", pady=4)
            tk.Label(row, text=f"  {k}", font=(self.FONT, 10, "bold"),
                     bg=self.CARD, fg=self.ACCENT, width=12, anchor="w").pack(side="left")
            tk.Label(row, text=v, font=(self.FONT, 10),
                     bg=self.CARD, fg=self.TEXT, anchor="w").pack(side="left")

    # ── title animation ──────────────────────────────────────────────────────

    def _animate_title(self):
        self._ti = 0
        frames = ["Fibonacci Generator — Hex Softwares",
                  "Fibonacci Generator — 0, 1, 1, 2, 3, 5, 8, 13 ..."]
        def step():
            self.title(frames[self._ti % 2])
            self._ti += 1
            self.after(3000, step)
        step()


if __name__ == "__main__":
    app = FibonacciApp()
    app.mainloop()
