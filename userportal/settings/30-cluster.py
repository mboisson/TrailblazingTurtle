EXPORTER_INSTALLED = [
    'slurm-job-exporter',
    'node_exporter',
    'redfish_exporter',
    'lfs_quota',
    'lustre_exporter',
    'slurm_exporter',
    'pcm-sensor-server',
]

EXPORTER_SAMPLING_RATE = {
    'slurm-job-exporter': 30,
    'node_exporter': 30,
    'redfish_exporter': 90,
    'lustre_exporter': 90,
    'slurm_exporter': 60,
    'pcm-sensor-server': 30,
}

CLUSTER_NAME = 'narval'  # used for slurm stats
STORAGE_NAME = 'narval-storage'
COMPUTE_NAME = 'narval'  # narval-compute or narval-gpu
LUSTRE_FS_NAMES = ['lustre05', 'lustre06', 'lustre07']
LOGINS = {
    'narval1': {
        'network_interface': 'eno34',
    },
    'narval2': {
        'network_interface': 'eno34',
    },
    'narval3': {
        'network_interface': 'eno34',
    },
}
DTNS = {
    'narval-dtn1': {
        'network_interface': 'bond0',
    },
    'narval-dtn2': {
        'network_interface': 'bond0',
    },
    'narval-dtn3': {
        'network_interface': 'bond0',
    },
    'narval-dtn4': {
        'network_interface': 'bond0',
    },
}

# value used in the next variables, not showned in the UI, can be removed
HARDWARE_OVERHEAD = 1.10  # cables, racks, etc.
CURRENCY_CONVERSION = 1.25  # USD to CAD conversion

# Can be set to None to disable the reporting
AMORTIZATION_YEARS = 5  # servers are amortized over 5 years
CPU_CORE_COST_PER_HOUR = 7500 / 64 / (365 * 24 * AMORTIZATION_YEARS) * HARDWARE_OVERHEAD
GPU_COST_PER_HOUR = 50000 / 4 / (365 * 24 * AMORTIZATION_YEARS) * HARDWARE_OVERHEAD

ELECTRICITY_COST_PER_KWH = (4.158 / 100)  # in $/kWh
COOLING_COST_PER_KWH = ELECTRICITY_COST_PER_KWH * 0.25  # not the exact value, but close enough
CO2_KG_PER_MWH = 0.5  # https://www.hydroquebec.com/data/developpement-durable/pdf/taux-emission-co2-approvisionnement-electricite-2020.pdf
ELECTRIC_CAR_RANGE_KM_PER_KWH = 1 / 0.151  # 151Wh/km https://ev-database.org/car/1555/Tesla-Model-3

CLOUD_CPU_CORE_COST_PER_HOUR = 2.448 / 64 * CURRENCY_CONVERSION  # c6a.16xlarge = 64 cores, 128GB, half the memory of Narval
CLOUD_GPU_COST_PER_HOUR = 5.672 / 4 * CURRENCY_CONVERSION  # g5.12xlarge = 48 cores, 4 GPUs, 192GB of ram, less than half the memory of Narval

# Used to set reasonable thresholds for the mem usage in the "top compute" page
NORMAL_MEM_BY_CORE = 256/64 * 1024 * 1024 * 1024  # 256GB for 64 cores
NORMAL_MEM_BY_GPU = 512 / 4 * 1024 * 1024 * 1024  # 512GB for 4 GPUs
NORMAL_CORES_BY_GPU = 48 / 4  # 48 cores for 4 GPUs

# Used to find the current quotas in prometheus
QUOTA_TYPES = {
    'home': ('/lustre05/home/', 'project'),
    'scratch': ('/lustre07/scratch/', 'project'),
    'project': ('/lustre06/project/', 'project'),
}

SLURM_TRES = {
    '1001=': 'NVIDIA A100-SXM4-40GB',
}

CLUSTER_NAME_TITLE = 'Narval'
FAVICON = 'https://object-arbutus.cloud.computecanada.ca/userportal-public/narval.png'

CLUSTER_INTRO = """
<p>Narval is a general purpose cluster designed for a variety of workloads; it is located at the <a href="https://www.etsmtl.ca/en/home">École de technologie supérieure in Montreal</a> and is managed by <a href="https://www.calculquebec.ca/">Calcul Québec</a>. The cluster is named in honour of the <a href="https://en.wikipedia.org/wiki/Narwhal">narwhal</a>, a species of whale which has occasionally been observed in the Gulf of St. Lawrence.</p>

<p>This cluster is composed of over 80720 cores and 636 GPUs, all nodes are connected at 100Gb/s.</p>

<p>This portal is intended for our users, the menu on the left provides multiple tools to measure job performance and current cluster utilization</p>

<p><a href="https://docs.computecanada.ca/wiki/Narval/">Documentation</a></p>
"""

CLOUD_ALLOCATIONS_FILE = '/var/www/userportal/projects-rac2022.yml'

# Links in the menu
EXTERNAL_LINKS = []
#EXTERNAL_LINKS = [
#    {'name': 'Documentation', 'url': 'https://docs.alliancecan.ca/wiki/Narval', 'icon': 'book'},
#    {'name': 'Globus', 'url': 'https://app.globus.org/file-manager?origin_id=a1713da6-098f-40e6-b3aa-034efe8b6e5b', 'icon': 'globe'},
#    {'name': 'JupyterHub', 'url': 'https://jupyterhub.narval.calculquebec.ca', 'icon': 'terminal'},
#]

# Links to other portals, under external links. 
# The path parameter enable compatibility with other portals by sending the user to the same page in the other portal
OTHER_PORTALS = []
#OTHER_PORTALS = [
#    {'name': 'Beluga', 'url': 'https://portail.beluga.calculquebec.ca', 'path': True},
#    {'name': 'Graham', 'url': 'https://dashboard.graham.sharcnet.ca', 'path': True},
#    {'name': 'Niagara', 'url': 'https://my.scinet.utoronto.ca', 'path': False},
#]

SOFTWARE_REGEX = [
    (r'.*/gmx_mpi$|.*/gmx$', 'GROMACS'),
    (r'.*/vasp$', 'VASP'),
    (r'.*/lammps$', 'LAMMPS'),
    (r'.*/cp2k$', 'CP2K'),
    (r'.*/nwchem$', 'NWChem'),
    (r'.*/namd2$', 'NAMD'),
    (r'.*/abinit$', 'ABINIT'),
    (r'.*/espresso$', 'Quantum Espresso'),
    (r'.*/gaussian$', 'Gaussian'),
    (r'.*/octopus$', 'Octopus'),
    (r'.*/orca$', 'ORCA'),
    (r'.*/qchem$', 'Q-Chem'),
    (r'.*/tinker$', 'Tinker'),
    (r'.*/amber$', 'Amber'),
    (r'.*/charmm$', 'CHARMM'),
    (r'.*/cpmd$', 'CPMD'),
    (r'.*/dftb$', 'DFTB+'),
    (r'.*/gamess$', 'GAMESS'),
    (r'.*/molcas$', 'Molcas'),
    (r'.*/molpro$', 'Molpro'),
    (r'.*/mpqc$', 'MPQC'),
    (r'.*/mopac$', 'MOPAC'),
    (r'.*/mpqc$', 'MPQC'),
    (r'.*/openmx$', 'OpenMX'),
    (r'.*/psi4$', 'Psi4'),
    (r'.*/qbox$', 'Qbox'),
    (r'.*/epw.x$', 'EPW'),
    (r'.*/python.*$', 'Python'),  # put all the versions of python together
    (r'.*/MATLAB$', 'MATLAB'),
    (r'.*/R$', 'R'),
    (r'.*/julia$', 'Julia'),
    (r'.*/java$', 'Java'),
    (r'.*/perl$', 'Perl'),
    (r'.*/maingemdm$', 'GEMDM'),
    (r'.*/maingem$', 'GEM'),
    (r'.*/pimpleFoam$', 'pimpleFoam'),
    (r'.*/simpleFoam$', 'simpleFoam'),
    (r'.*/icoFoam$', 'icoFoam'),
    (r'.*/interFoam$', 'interFoam'),
    (r'.*/topas$', 'Topas'),
    (r'.*/OstrichMPI$', 'Ostrich'),
    (r'.*/pb_mpi$', 'PhyloBayes'),
    (r'.*/gh3d2m$', 'gh3d2m'),
    (r'.*/dmft$', 'DMFT'),
    (r'.*/pw.x$', 'Quantum Espresso'),
    (r'.*/siesta$', 'SIESTA'),
    (r'.*/bcftools$', 'BCFTools'),
    (r'.*/samtools$', 'SAMTools'),
    (r'.*/bowtie2$', 'Bowtie2'),
    (r'.*/bwa$', 'BWA'),
    (r'.*/vcftools$', 'VCFTools'),
    (r'.*/nc(ap2|atted|bo|climo|es|ecat|flint|ks|pdq|ra|rcat|remap|rename|wa)$', 'NCO'),
]

SOFTWARE_STACK_REGEX = [
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2017/Core/.*', '2017 - Core'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2017/sse3/.*', '2017 - SSE3'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2017/avx/.*', '2017 - AVX'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2017/avx2/.*', '2017 - AVX2'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2017/avx512/.*', '2017 - AVX512'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2019/Core/.*', '2019 - Core'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2020/Core/.*', '2020 - Core'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2020/avx/.*', '2020 - AVX'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2020/avx2/.*', '2020 - AVX2'),
    (r'/cvmfs/.*.computecanada.ca/easybuild/software/2020/avx512/.*', '2020 - AVX512'),
    (r'/cvmfs/.*.computecanada.ca/gentoo/2020/.*', '2020 - Gentoo'),
]

POSIX_PERSONAL_GROUP_USAGE_NOTE = 'Files should not be stored on the project filesystem with a personal group. <a href="https://docs.alliancecan.ca/wiki/Frequently_Asked_Questions#Disk_quota_exceeded_error_on_/project_filesystems">Learn More</a>'

LOCALSCRATCH = '/localscratch'