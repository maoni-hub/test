"""
完整演示脚本 - 生成所有14个光纤传感器示意图
"""

from fiber_optic_plotting import InstrumentDiagrams, OpticalSystems, FiberConfigurations
import os


def generate_all_diagrams():
    """生成所有光纤传感器示意图"""
    
    print("=" * 60)
    print("光纤传感器绘图库 - 完整演示")
    print("=" * 60)
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # ========== 仪器结构图 (5个) ==========
    print("\n【仪器结构图】")
    
    diagrams = InstrumentDiagrams()
    
    # 1. Fabry-Perot干涉仪
    print("1. 生成 Fabry-Perot干涉仪...")
    diagrams.fabry_perot_interferometer()
    diagrams.save_figure("output/01_fabry_perot_interferometer.png")
    
    # 2. FBG传感系统
    print("2. 生成 FBG传感系统...")
    diagrams.fbg_sensor_system()
    diagrams.save_figure("output/02_fbg_sensor_system.png")
    
    # 3. Mach-Zehnder干涉仪
    print("3. 生成 Mach-Zehnder干涉仪...")
    diagrams.mach_zehnder_interferometer()
    diagrams.save_figure("output/03_mach_zehnder_interferometer.png")
    
    # 4. 分布式光纤传感(DAS)
    print("4. 生成 分布式光纤传感系统...")
    diagrams.distributed_fiber_sensing()
    diagrams.save_figure("output/04_distributed_fiber_sensing.png")
    
    # 5. 本征Fabry-Perot传感器
    print("5. 生成 本征Fabry-Perot传感器...")
    diagrams.intrinsic_fabry_perot()
    diagrams.save_figure("output/05_intrinsic_fabry_perot.png")
    
    # ========== 光学系统示意图 (4个) ==========
    print("\n【光学系统示意图】")
    
    systems = OpticalSystems()
    
    # 6. 光学路径系统
    print("6. 生成 光学路径系统...")
    systems.optical_path_system()
    systems.save_figure("output/06_optical_path_system.png")
    
    # 7. 白光干涉系统
    print("7. 生成 白光干涉系统...")
    systems.white_light_interference()
    systems.save_figure("output/07_white_light_interference.png")
    
    # 8. 波分复用(WDM)系统
    print("8. 生成 波分复用系统...")
    systems.wavelength_division_multiplexing()
    systems.save_figure("output/08_wavelength_division_multiplexing.png")
    
    # 9. 频域反射仪(FDR)
    print("9. 生成 频域反射仪系统...")
    systems.frequency_domain_reflectometry()
    systems.save_figure("output/09_frequency_domain_reflectometry.png")
    
    # ========== 光纤配置图 (5个) ==========
    print("\n【光纤配置图】")
    
    configs = FiberConfigurations()
    
    # 10. 单模光纤横截面
    print("10. 生成 单模光纤横截面...")
    configs.single_mode_fiber_cross_section()
    configs.save_figure("output/10_single_mode_fiber_cross_section.png")
    
    # 11. 多模光纤横截面
    print("11. 生成 多模光纤横截面...")
    configs.multimode_fiber_cross_section()
    configs.save_figure("output/11_multimode_fiber_cross_section.png")
    
    # 12. 侧面抛光光纤
    print("12. 生成 侧面抛光光纤...")
    configs.side_polished_fiber()
    configs.save_figure("output/12_side_polished_fiber.png")
    
    # 13. 倾斜光纤布拉格光栅(TFBG)
    print("13. 生成 倾斜FBG...")
    configs.tilted_fiber_bragg_grating()
    configs.save_figure("output/13_tilted_fiber_bragg_grating.png")
    
    # 14. 长周期光栅(LPG)
    print("14. 生成 长周期光栅...")
    configs.long_period_grating()
    configs.save_figure("output/14_long_period_grating.png")
    
    # ========== 完成 ==========
    print("\n" + "=" * 60)
    print("✓ 所有14个图表生成完成！")
    print("=" * 60)
    print("\n输出文件位置: ./output/")
    print("\n生成的文件:")
    print("  仪器结构图 (5个):")
    print("    - Fabry-Perot干涉仪")
    print("    - FBG传感系统")
    print("    - Mach-Zehnder干涉仪")
    print("    - 分布式光纤传感系统")
    print("    - 本征Fabry-Perot传感器")
    print("\n  光学系统示意图 (4个):")
    print("    - 光学路径系统")
    print("    - 白光干涉系统")
    print("    - 波分复用(WDM)系统")
    print("    - 频域反射仪(FDR)系统")
    print("\n  光纤配置图 (5个):")
    print("    - 单模光纤横截面")
    print("    - 多模光纤横截面")
    print("    - 侧面抛光光纤")
    print("    - 倾斜FBG")
    print("    - 长周期光栅")


if __name__ == "__main__":
    generate_all_diagrams()
