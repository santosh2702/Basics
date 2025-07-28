📁 Project
├── 📦 Models (📊 Data Layer)
│   ├── 👤 User.cs
│   ├── 📦 Product.cs
│   └── 🧾 Order.cs
│
├── 🎮 Controllers (🧭 API Layer)
│   ├── 👤 UserController.cs
│   ├── 📦 ProductController.cs
│   └── 🧾 OrderController.cs
│
├── 🧠 Services (🧮 Business Logic Layer)
│   ├── 🧩 IUserService.cs      (🔌 Interface)
│   ├── 🧠 UserService.cs       (⚙️ Implementation)
│   ├── 🧠 ProductService.cs
│   └── 🧠 OrderService.cs
│
├── 🗄️ Data Access Layer (📚 Repository)
│   ├── 🧩 IUserRepository.cs
│   ├── 🗄️ UserRepository.cs
│   ├── 🗄️ ProductRepository.cs
│   └── 🗄️ OrderRepository.cs
│
├── 🧰 Dependency Injection Setup
│   └── 🛠️ Program.cs / Startup.cs
│
└── 🧩 Utilities (🛎️ Helper classes, 🔌 extensions)
    ├── 🪵 Logger.cs
    └── 📦 ResponseWrapper.cs
