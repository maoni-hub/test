"""
Optical Systems - 光学系统示意图
包括各种光学系统和光路配置的示意图
"""

from .base_plotter import BasePlotter
import matplotlib.patches as patches


class OpticalSystems(BasePlotter):
    """光学系统示意图绘制类"""
    
    def optical_path_system(self):
        """绘制光学路径系统"""
        self.clear()
        self.set_axis_properties(
            xlim=(0, 14),
            ylim=(0, 10),
            title="Optical Path System (光学路径系统)"
        )
        
        # 光源
        self.draw_component(1, 5, 0.8, 0.8, 'circle', 'Light\nSource', 'yellow')
        self.draw_arrow(1.5, 5, 2.5, 5, 'Coherent\nLight')
        
        # 透镜1 (准直)
        self.draw_component(3, 5, 0.4, 1.5, 'box', 'L1', 'lightblue')
        self.ax.text(3, 6.5, 'Collimation', fontsize=8, ha='center')
        self.draw_arrow(3.3, 5, 4.3, 5, 'Collimated\nBeam')
        
        # 分光镜
        self.draw_component(5, 5, 1, 1, 'diamond', 'BS\n(50/50)', 'lightgreen')
        self.draw_arrow(4.3, 5, 4.5, 5)
        
        # 反射光路 - 参考路径
        self.draw_arrow(5, 5.5, 5, 6.5, 'Reference\nPath')
        self.draw_component(5, 7, 0.8, 0.8, 'circle', 'M1', 'silver')
        self.draw_arrow(5, 6.5, 5, 5.5)
        
        # 透射光路 - 测量路径
        self.draw_arrow(5.5, 5, 6.5, 5, 'Measurement\nPath')
        self.draw_component(7, 5, 1, 1, 'box', 'Sample', 'lightcoral')
        self.draw_arrow(7.5, 5, 8.5, 5)
        self.draw_component(9, 5, 0.8, 0.8, 'circle', 'M2', 'silver')
        
        # 回程
        self.draw_arrow(9, 4.5, 9, 2.5, 'Return\nPath')
        self.draw_arrow(9, 2.5, 5, 2.5)
        self.draw_arrow(5, 2.5, 5, 4.5)
        
        # 分光镜合束
        self.draw_arrow(5, 4.5, 5, 4.5)
        
        # 透镜2 (聚焦)
        self.draw_arrow(5.5, 5, 6.5, 5)
        self.draw_component(7, 5, 0.4, 1.5, 'box', 'L2', 'lightblue')
        self.ax.text(7, 6.5, 'Focusing', fontsize=8, ha='center')
        self.draw_arrow(7.3, 5, 8.3, 5)
        
        # 检测器
        self.draw_component(9, 5, 1, 1, 'circle', 'Detector', 'lightblue')
    
    def white_light_interference(self):
        """绘制白光干涉系统"""
        self.clear()
        self.set_axis_properties(
            xlim=(0, 14),
            ylim=(0, 10),
            title="White Light Interferometry (白光干涉系统)"
        )
        
        # 白光源
        self.draw_component(1, 5, 0.8, 0.8, 'circle', 'White\nLight', 'yellow')
        self.draw_arrow(1.5, 5, 2.5, 5)
        
        # 分光镜
        self.draw_component(3, 5, 1, 1, 'diamond', 'BS', 'lightgreen')
        
        # 参考臂
        self.draw_arrow(3, 5.5, 3, 6.5)
        self.draw_component(3, 7, 0.6, 0.6, 'box', 'Ref\nMirror', 'silver')
        self.draw_arrow(3, 6.5, 3, 5.5)
        self.ax.text(2.2, 6, 'Reference\nArm', fontsize=8)
        
        # 测量臂
        self.draw_arrow(3.5, 5, 4.5, 5)
        self.draw_component(5, 5, 1.2, 0.8, 'box', 'Measurement\nSurface', 'lightcoral')
        self.draw_arrow(5.6, 5, 6.5, 5)
        
        # 回程
        self.draw_arrow(6.5, 5, 7.5, 5)
        self.draw_arrow(7.5, 5, 8.5, 4.5)
        self.draw_arrow(8.5, 4.5, 3, 4.5)
        self.draw_arrow(3, 4.5, 3, 4.5)
        
        # 干涉
        self.draw_component(9, 5, 1.5, 1, 'box', 'Interference\nFringes', 'lightyellow')
        self.draw_arrow(8.5, 5, 8.2, 5)
        
        # 检测和处理
        self.draw_component(11, 5, 1.5, 1, 'box', 'Detector +\nProcessing', 'lightgray')
        self.draw_arrow(10.2, 5, 10.2, 5)
        
        # 输出
        self.draw_component(13, 5, 1, 1, 'box', 'Height/\nDistance', 'palegreen')
    
    def wavelength_division_multiplexing(self):
        """绘制波分复用(WDM)系统"""
        self.clear()
        self.set_axis_properties(
            xlim=(0, 14),
            ylim=(0, 10),
            title="Wavelength Division Multiplexing (波分复用系统)"
        )
        
        # 输入光源
        self.draw_component(1, 7, 0.6, 0.6, 'circle', 'λ1', 'red')
        self.draw_component(1, 5, 0.6, 0.6, 'circle', 'λ2', 'green')
        self.draw_component(1, 3, 0.6, 0.6, 'circle', 'λ3', 'blue')
        
        # 光纤连接
        self.draw_optical_fiber(1.4, 7, 2.5, 6.5)
        self.draw_optical_fiber(1.4, 5, 2.5, 5)
        self.draw_optical_fiber(1.4, 3, 2.5, 3.5)
        
        # WDM复用器
        self.draw_component(3.5, 5, 1.2, 1.5, 'box', 'WDM\nMux', 'lightyellow')
        self.draw_optical_fiber(2.5, 6.5, 3, 5.5)
        self.draw_optical_fiber(2.5, 5, 3, 5)
        self.draw_optical_fiber(2.5, 3.5, 3, 4.5)
        
        # 复用光纤
        self.draw_optical_fiber(4.1, 5, 6, 5, label='Multiplexed\nSignal')
        
        # 传输
        self.draw_optical_fiber(6, 5, 8, 5)
        
        # WDM分解器
        self.draw_component(9, 5, 1.2, 1.5, 'box', 'WDM\nDemux', 'lightyellow')
        self.draw_optical_fiber(8, 5, 8.5, 5)
        
        # 输出分离
        self.draw_optical_fiber(9.5, 5.5, 11, 6.5)
        self.draw_optical_fiber(9.5, 5, 11, 5)
        self.draw_optical_fiber(9.5, 4.5, 11, 3.5)
        
        # 输出检测器
        self.draw_component(11.5, 6.5, 0.6, 0.6, 'circle', 'PD1', 'red')
        self.draw_component(11.5, 5, 0.6, 0.6, 'circle', 'PD2', 'green')
        self.draw_component(11.5, 3.5, 0.6, 0.6, 'circle', 'PD3', 'blue')
    
    def frequency_domain_reflectometry(self):
        """绘制频域反射仪(FDR)系统"""
        self.clear()
        self.set_axis_properties(
            xlim=(0, 14),
            ylim=(0, 10),
            title="Frequency Domain Reflectometry (频域反射仪系统)"
        )
        
        # RF信号源
        self.draw_component(1, 5, 0.8, 0.8, 'circle', 'RF\nSource', 'yellow')
        self.draw_arrow(1.5, 5, 2.5, 5, 'RF\nSignal')
        
        # 光调制器
        self.draw_component(3.5, 5, 1, 0.8, 'box', 'Optical\nModulator', 'lightgreen')
        self.draw_optical_fiber(1, 3.5, 3, 4.2)
        self.ax.text(1.5, 3, 'Laser', fontsize=8, ha='center')
        
        # 耦合器
        self.draw_component(5, 5, 0.8, 0.8, 'box', 'Coupler', 'lightblue')
        self.draw_optical_fiber(4.2, 5, 4.6, 5)
        
        # 传感光纤
        self.draw_optical_fiber(5.4, 5, 8, 5, label='Sensing Fiber\n(with defects)')
        
        # 缺陷/断点标记
        for x_pos in [6, 7]:
            self.draw_component(x_pos, 5.3, 0.3, 0.3, 'circle', '', 'red')
        
        # 返回信号
        self.draw_optical_fiber(8, 5, 9, 4.8)
        self.draw_optical_fiber(9, 4.8, 9, 3.5)
        
        # 光电检测
        self.draw_component(9.5, 3, 0.8, 0.8, 'circle', 'Photo\nDetector', 'lightblue')
        self.draw_arrow(9, 3, 8.7, 3)
        
        # 信号处理和分析
        self.draw_component(11, 3, 1.5, 1.2, 'box', 'Signal\nProcessing\n& Analysis', 'lightgray')
        self.draw_arrow(10, 3, 10.2, 3)
        
        # 输出显示
        self.draw_component(12.5, 5, 1.2, 1, 'box', 'Distance/\nAttenuation\nProfile', 'palegreen')
        self.draw_arrow(11.75, 3.5, 12.5, 4.5)
