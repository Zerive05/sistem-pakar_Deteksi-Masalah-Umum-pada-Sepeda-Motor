% Basis pengetahuan untuk deteksi masalah umum pada sepeda motor

start :-
    write('=== Sistem Pakar Deteksi Masalah Sepeda Motor ==='), nl,
    write('Jawab pertanyaan berikut dengan ya atau tidak.'), nl,
    konsultasi.

konsultasi :-
    masalah(Masalah),
    write('Kemungkinan masalah pada motor Anda adalah: '), write(Masalah), nl.
konsultasi :-
    write('Maaf, sistem tidak dapat menentukan masalah motor Anda.'), nl.

% Aturan penentuan masalah
masalah(busi_mati) :-
    tanya(motor_sulit_dihidupkan),
    tanya(tidak_ada_letupan_di_knalpot).

masalah(karburator_kotor) :-
    tanya(mesin_tersendat),
    tanya(boros_bensin).

masalah(aki_lemah) :-
    tanya(lampu_redup),
    tanya(klakson_lemah).

masalah(kampas_rem_habis) :-
    tanya(rem_tidak_pakem),
    tanya(ada_suara_berdecit).

% Fakta gejala berdasarkan input pengguna
:- dynamic(ya/1).
:- dynamic(tidak/1).

tanya(X) :- ya(X), !.
tanya(X) :- tidak(X), !, fail.
tanya(X) :-
    write(X), write('? (ya/tidak): '),
    read(Jawaban),
    nl,
    (Jawaban == ya -> assertz(ya(X));
     assertz(tidak(X)), fail).

% Reset fakta
hapus_fakta :- retract(ya(_)), fail.
hapus_fakta :- retract(tidak(_)), fail.
hapus_fakta.
