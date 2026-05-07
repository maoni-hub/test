"""
Fiber Configurations - 光纤配置示意图
包括各种光纤类型和配置方案的示意图
"""

from .base_plotter import BasePlotter
import matplotlib.patches as patches
import numpy as np


class FiberConfigurations(BasePlotter):
    """光纤配置示意图绘制类"""
    
    def single_mode_fiber_cross_section(self):
        """绘制单模光纤(SMF)横截面"""
        self.clear()
        self.set_axis_properties(
            xlim=(-8, 8),
            ylim=(-8, 8),
            title="Single Mode Fiber (SMF) Cross-Section (单模光纤横截面)",
            equal_aspect=True
        )
        
        # 外套 (Jacket)
        jacket = patches.Circle((0, 0), 7, fill=True, 
                               edgecolor='black', facecolor='lightyellow', linewidth=2)
        self.ax.add_patch(jacket)
        self.ax.text(0, -7.5, 'Jacket (125 μm)', fontsize=9, ha='center')
        
        # 包层 (Cladding)
        cladding = patches.Circle((0, 0), 5, fill=True, 
                                 edgecolor='darkblue', facecolor='lightblue', linewidth=2)
        self.ax.add_patch(cladding)
        
        # 纤芯 (Core)
        core = patches.Circle((0, 0), 0.6, fill=True, 
                             edgecolor='darkred', facecolor='red', linewidth=2)
        self.ax.add_patch(core)
        self.ax.text(0, 0, 'Core\n~8-10 μm', fontsize=8, ha='center', va='center', color='white', weight='bold')
        
        # 标注线
        self.ax.plot([-0.6, -3], [0, 0], 'k--', linewidth=1)
        self.ax.text(-3.5, 0.5, 'Core', fontsize=9)
        
        self.ax.plot([-5, -6.5], [0, 0], 'k--', linewidth=1)
        self.ax.text(-7, 0.5, 'Cladding', fontsize=9)
        
        self.ax.plot([5, 6.5], [0, 0], 'k--', linewidth=1)
        self.ax.text(6.8, 0.5, 'Cladding', fontsize=9)
    
    def multimode_fiber_cross_section(self):
        """绘制多模光纤(MMF)横截面"""
        self.clear()
        self.set_axis_properties(
            xlim=(-10, 10),
            ylim=(-10, 10),
            title="Multimode Fiber (MMF) Cross-Section (多模光纤横截面)",
            equal_aspect=True
        )
        
        # 外套
        jacket = patches.Circle((0, 0), 9, fill=True, 
                               edgecolor='black', facecolor='lightyellow', linewidth=2)
        self.ax.add_patch(jacket)
        self.ax.text(0, -9.5, 'Jacket (250 μm)', fontsize=9, ha='center')
        
        # 包层
        cladding = patches.Circle((0, 0), 6, fill=True, 
                                 edgecolor='darkblue', facecolor='lightblue', linewidth=2)
        self.ax.add_patch(cladding)
        
        # 纤芯 (大多数光线)
        core = patches.Circle((0, 0), 3.5, fill=True, 
                             edgecolor='darkred', facecolor='yellow', linewidth=2, alpha=0.7)
        self.ax.add_patch(core)
        
        # 绘制多条光路
        modes = [
            (0, 0),  # 轴向模式
            (1.5, 1),
            (1, -1.5),
            (-1.5, 1),
            (-1, -1.5),
            (2, 0),
            (-2, 0)
        ]
        
        for x, y in modes:
            self.ax.plot(x, y, 'r.', markersize=8)
        
        self.ax.text(0, 0, 'Multiple\nModes', fontsize=9, ha='center', va='center', weight='bold')
        self.ax.text(0, 3.8, 'Core ~50-62.5 μm', fontsize=8, ha='center')
        
        # 标注
        self.ax.annotate('', xy=(3.5, -5), xytext=(0, -5),
                        arrowprops=dict(arrowstyle='<->', color='black'))
        self.ax.text(1.75, -5.5, 'Core diameter', fontsize=8, ha='center')
    
    def side_polished_fiber(self):
        """绘制侧面抛光光纤配置"""
        self.clear()
        self.set_axis_properties(
            xlim=(0, 14),
            ylim=(0, 10),
            title="Side-Polished Fiber Configuration (侧面抛光光纤配置)"
        )
        
        # 光纤输入
        self.draw_optical_fiber(0.5, 5, 2, 5, label='Input')
        
        # 侧面抛光段
        y_positions = np.linspace(4.7, 5.3, 5)
        for i, y in enumerate(y_positions):
            x = 2.5 + i * 0.8
            if i % 2 == 0:
                self.draw_component(x, y, 0.6, 0.6, 'box', '', 'lightcoral')
        
        # 敏感材料涂层
        self.ax.text(5, 6.2, 'Sensitive Coating\n(Metal/Polymer)', fontsize=9, ha='center',
                    bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
        
        # 光纤继续
        self.draw_optical_fiber(6.5, 5, 10, 5, label='Output')
        
        # 传感机制标注
        self.draw_component(7, 3.5, 1.2, 0.8, 'box', 'Analyte\nContact', 'lightyellow')
        self.ax.annotate('', xy=(6.2, 4.2), xytext=(6.2, 3.9),
                        arrowprops=dict(arrowstyle='<->', color='blue'))
        self.ax.text(5.5, 4.1, 'Evanescent\nWave', fontsize=8, ha='center', color='blue')
        
        # 输出说明
        self.ax.text(10.5, 5, 'Intensity\nChange', fontsize=9, ha='center',
                    bbox=dict(boxstyle='round', facecolor='palegreen', alpha=0.7))
    
    def tilted_fiber_bragg_grating(self):
        """绘制倾斜光纤布拉格光栅(Tilted FBG)"""
        self.clear()
        self.set_axis_properties(
            xlim=(0, 14),
            ylim=(0, 10),
            title="Tilted Fiber Bragg Grating (TFBG) (倾斜光纤布拉格光栅)"
        )
        
        # 光纤
        self.draw_optical_fiber(0.5, 5, 3, 5)
        
        # 光栅区域
        grating_start = 3
        grating_end = 9
        
        # 绘制倾斜光栅
        num_gratings = 15
        for i in range(num_gratings):
            x1 = grating_start + (grating_end - grating_start) * i / num_gratings
            x2 = x1 + 0.3
            y1 = 4.8 + 0.3 * np.sin(np.pi * i / num_gratings)
            y2 = 5.2 + 0.3 * np.sin(np.pi * i / num_gratings)
            
            self.ax.plot([x1, x2], [y1, y2], 'b-', linewidth=2)
        
        self.ax.text(6, 6.2, 'Tilted Grating\n(45°)', fontsize=10, ha='center', 
                    bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        
        # 反射光
        self.draw_optical_fiber(6, 5.5, 6, 8, linestyle='--', label='Reflected\nCladiing Modes')
        
        # 输出光
        self.draw_optical_fiber(9, 5, 12, 5, label='Output')
        
        # 传感说明
        self.ax.text(13, 5, 'Multimodal\nResponse', fontsize=9, ha='center',
                    bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    def long_period_grating(self):
        """绘制长周期光栅(LPG)"""
        self.clear()
        self.set_axis_properties(
            xlim=(0, 14),
            ylim=(0, 10),
            title="Long Period Grating (LPG) (长周期光栅)"
        )
        
        # 光纤输入
        self.draw_optical_fiber(0.5, 5, 2, 5, label='Core Mode')
        
        # LPG区域
        self.ax.add_patch(patches.Rectangle((2, 4.5), 6, 1, 
                                           fill=True, facecolor='lightyellow', 
                                           edgecolor='black', linewidth=2))
        
        # 绘制LPG周期性结构
        period = 0.6
        num_periods = 10
        for i in range(num_periods):
            x = 2.2 + i * period
            # 上下波动
            y_top = 5 + 0.3
            y_bot = 5 - 0.3
            self.ax.plot([x, x + 0.2], [y_top, y_bot], 'b-', linewidth=2)
        
        self.ax.text(5, 5.8, 'Periodic Modulation\nPeriod: ~100-500 μm', 
                    fontsize=9, ha='center')
        
        # 模式转换
        self.ax.text(8.5, 6.5, 'Core Mode → Cladding Mode\n(Resonant Coupling)', 
                    fontsize=9, ha='center',
                    bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
        
        # 耦合到包层的光
        self.ax.arrow(8, 5.5, 1, 1.5, head_width=0.3, head_length=0.2, fc='green', ec='green')
        
        # 输出 (透射光和耦合光)
        self.draw_optical_fiber(8, 5, 12, 5, label='Transmitted Core Mode')
        self.draw_optical_fiber(9, 6.5, 12, 7, linestyle='--', label='Cladding Modes')
