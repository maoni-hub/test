# 光纤传感器绘图库 (Fiber Optic Plotting Library)

一套专业的Python绘图库，用于生成光纤传感器的仪器结构图、光学系统示意图和光纤配置图。

## 🎯 功能特性

- ✨ 14个预制图表模板
- 🎨 专业级的光学系统可视化
- 📊 支持高分辨率输出 (300-600 DPI)
- 🔧 易于集成和自定义
- 📖 完整的中英文文档和示例

## 📦 包含的图表

### 仪器结构图 (5个)
1. **Fabry-Perot干涉仪** - 经典的光纤干涉式传感器
2. **FBG传感系统** - 多点分布式光纤布拉格光栅传感器
3. **Mach-Zehnder干涉仪** - 两臂干涉仪配置
4. **分布式光纤传感(DAS)** - 沿光纤的分布式声学传感
5. **本征Fabry-Perot传感器** - 光纤内部的法布里-珀罗腔

### 光学系统示意图 (4个)
6. **光学路径系统** - 从光源到检测器的完整光路
7. **白光干涉系统** - 参考臂和测量臂配置
8. **波分复用(WDM)** - 多波长光信号的复用/分解
9. **频域反射仪(FDR)** - 光纤缺陷和衰减检测系统

### 光纤配置图 (5个)
10. **单模光纤(SMF)横截面** - 纤芯/包层/外套结构
11. **多模光纤(MMF)横截面** - 多模传播示意
12. **侧面抛光光纤** - 敏感区域和倘逸波耦合
13. **倾斜光纤布拉格光栅(Tilted FBG)** - 模式转换配置
14. **长周期光栅(LPG)** - 纤芯模到包层模的耦合

## 🚀 快速开始

### 安装

```bash
# 克隆或下载仓库
cd test

# 安装依赖
pip install -r requirements.txt
```

### 基础使用

```python
from fiber_optic_plotting import InstrumentDiagrams

# 创建绘图器
diagrams = InstrumentDiagrams()

# 绘制FBG传感系统
diagrams.fbg_sensor_system()

# 保存为PNG文件 (300 DPI)
diagrams.save_figure('output/fbg_system.png')
```

### 生成所有图表

```bash
python examples/demo_all_diagrams.py
```

这会在 `output/` 文件夹生成所有14个图表。

### 高分辨率输出 (用于论文)

```python
from fiber_optic_plotting import InstrumentDiagrams

# 创建高分辨率绘图器 (600 DPI, 16x12英寸)
diagrams = InstrumentDiagrams(figsize=(16, 12), dpi=600)

diagrams.fbg_sensor_system()
diagrams.save_figure('output/fbg_hires.png')
```

## 📚 详细使用

### 仪器结构图类

```python
from fiber_optic_plotting import InstrumentDiagrams

diagrams = InstrumentDiagrams()

# 所有可用方法:
diagrams.fabry_perot_interferometer()          # Fabry-Perot干涉仪
diagrams.fbg_sensor_system()                   # FBG传感系统
diagrams.mach_zehnder_interferometer()         # Mach-Zehnder干涉仪
diagrams.distributed_fiber_sensing()           # 分布式光纤传感
diagrams.intrinsic_fabry_perot()               # 本征Fabry-Perot传感器

# 保存
diagrams.save_figure('output/diagram.png', dpi=300)
```

### 光学系统类

```python
from fiber_optic_plotting import OpticalSystems

systems = OpticalSystems()

# 所有可用方法:
systems.optical_path_system()                  # 光学路径系统
systems.white_light_interference()             # 白光干涉
systems.wavelength_division_multiplexing()     # WDM波分复用
systems.frequency_domain_reflectometry()       # FDR频域反射仪

systems.save_figure('output/optical_system.png')
```

### 光纤配置类

```python
from fiber_optic_plotting import FiberConfigurations

fiber = FiberConfigurations()

# 所有可用方法:
fiber.single_mode_fiber_cross_section()        # 单模光纤
fiber.multimode_fiber_cross_section()          # 多模光纤
fiber.side_polished_fiber()                    # 侧面抛光光纤
fiber.tilted_fiber_bragg_grating()             # 倾斜FBG
fiber.long_period_grating()                    # 长周期光栅

fiber.save_figure('output/fiber_config.png')
```

## 🤖 与Claude Code集成

### 步骤1: 在Claude中设置系统提示

告诉Claude关于这个库的信息：

```
我有一个Python模块 fiber_optic_plotting，可以生成光纤传感器示意图。

【可用的类】
- InstrumentDiagrams: 仪器结构图
- OpticalSystems: 光学系统图
- FiberConfigurations: 光纤配置图

【使用示例】
from fiber_optic_plotting import InstrumentDiagrams
diagrams = InstrumentDiagrams()
diagrams.fbg_sensor_system()
diagrams.save_figure('output/diagram.png')

当我需要生成图表时，请提供完整的Python代码。
```

### 步骤2: 提出绘图需求

```
我需要为我的论文生成一个FBG传感系统的原理图。

请提供完整的Python代码：
- 使用 FiberConfigurations.fbg_sensor_system()
- 分辨率: 600 DPI
- 输出文件: output/fbg_paper.png
```

### 步骤3: Claude生成代码

Claude会返回可以直接运行的完整代码！

## 📋 文件结构

```
test/
├── fiber_optic_plotting/        # 核心库
│   ├── __init__.py              # 模块初始化
│   ├── base_plotter.py          # 基础绘图类
│   ├── instrument_diagrams.py   # 仪器图 (5个)
│   ├── optical_systems.py       # 光学系统图 (4个)
│   └── fiber_configurations.py  # 光纤配置图 (5个)
│
├── examples/                    # 示例脚本
│   ├── quick_start.py           # 快速开始 (交互式)
│   └── demo_all_diagrams.py     # 完整演示 (生成全部)
│
├── requirements.txt             # Python依赖
├── README.md                    # 本文件
└── .gitignore                   # Git配置
```

## 🔧 自定义图表

### 修改图表大小和分辨率

```python
# 创建自定义大小的绘图器
diagrams = InstrumentDiagrams(figsize=(20, 14), dpi=600)
diagrams.fbg_sensor_system()
diagrams.save_figure('output/large_diagram.png')
```

### 基础绘图工具 (在BasePlotter中)

```python
from fiber_optic_plotting import BasePlotter

plotter = BasePlotter()

# 可用的基础方法
plotter.draw_arrow(x1, y1, x2, y2, label="Light")
plotter.draw_component(x, y, width, height, shape='box', label="Component")
plotter.draw_optical_fiber(x1, y1, x2, y2, label="Fiber")
plotter.draw_grating(x, y, length, spacing=0.1)
plotter.set_axis_properties(xlim, ylim, title, equal_aspect=True)
```

## 📝 示例代码

### 示例1: 生成单个图表

```python
from fiber_optic_plotting import FiberConfigurations

configs = FiberConfigurations()
configs.single_mode_fiber_cross_section()
configs.save_figure('output/smf.png')
```

### 示例2: 生成对比图表

```python
from fiber_optic_plotting import FiberConfigurations

fiber = FiberConfigurations()

# 单模光纤
fiber.single_mode_fiber_cross_section()
fiber.save_figure('output/smf.png')

# 多模光纤
fiber.multimode_fiber_cross_section()
fiber.save_figure('output/mmf.png')
```

### 示例3: 生成论文级图表

```python
from fiber_optic_plotting import InstrumentDiagrams

# 高质量设置
diagrams = InstrumentDiagrams(figsize=(16, 12), dpi=600)

# 绘制
diagrams.fbg_sensor_system()

# 保存为高分辨率
diagrams.save_figure('output/paper_figure_1.png', dpi=600)
```

## 💾 输出选项

### 保存分辨率

```python
# 默认分辨率 (100 DPI)
diagrams.save_figure('output/screen.png')

# 屏幕显示 (150 DPI)
diagrams.save_figure('output/display.png', dpi=150)

# 论文/印刷 (300 DPI)
diagrams.save_figure('output/paper.png', dpi=300)

# 高质量 (600 DPI)
diagrams.save_figure('output/hires.png', dpi=600)
```

## 🐛 故障排除

### 导入错误

```
ModuleNotFoundError: No module named 'fiber_optic_plotting'
```

**解决**: 确保在项目目录中运行代码，或添加路径：

```python
import sys
sys.path.append('/path/to/test')
from fiber_optic_plotting import InstrumentDiagrams
```

### 依赖缺失

```
ModuleNotFoundError: No module named 'matplotlib'
```

**解决**: 安装依赖

```bash
pip install -r requirements.txt
```

### 输出目录不存在

```
FileNotFoundError: [Errno 2] No such file or directory: 'output/diagram.png'
```

**解决**: 创建输出目录

```python
import os
os.makedirs('output', exist_ok=True)
```

## 📖 依赖

- Python 3.7+
- matplotlib >= 3.5.0
- numpy >= 1.21.0
- plotly >= 5.0.0 (可选，用于交互式图表)
- scipy >= 1.7.0 (可选)

## 🎓 学习资源

- [Matplotlib官方文档](https://matplotlib.org/)
- [光纤传感基础](https://en.wikipedia.org/wiki/Fiber_optic_sensor)
- [FBG传感器](https://en.wikipedia.org/wiki/Fiber_Bragg_grating)

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交问题和改进建议！

## 👨‍💻 作者

Fiber Optic Research Team

## ✨ 更新日志

### v1.0.0 (2026-05-07)
- 初始版本发布
- 14个预制图表模板
- 完整的中英文文档
- Claude Code集成指南

---

**快开始为你的光纤传感器研究生成专业级的示意图吧！** 🚀📊
