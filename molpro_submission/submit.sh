#!/bin/bash
#PBS -l walltime=00:15:00
#PBS -l nodes=1:ppn=1
#PBS -N 18000_11_ccsd
#PBS -j oe
#PBS -o /panfs/panasas01/chem/sa16246/calculations/isopentane_cn_dft/cn_isopentane_molpro_outputs/

# record some potentially useful details about the job:
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo PBS job ID is $PBS_JOBID
echo This jobs runs on the following machines: echo `cat $PBS_NODEFILE | uniq`

cd $PBS_O_WORKDIR

# The actual command
/panfs/panasas01/chem/sb13343/Molpro/bin/molpro -W /local -d /local  --no-xml-output /panfs/panasas01/chem/sa16246/calculations/isopentane_cn_dft/cn_isopentane_molpro_inputs/18000_11_ccsd.com