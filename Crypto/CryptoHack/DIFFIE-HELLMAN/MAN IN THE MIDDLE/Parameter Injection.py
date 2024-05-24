g = 2
A = "0x3b659d1fccb1507dbc1dea49da6cfec5e516624832c8aa61592b70f855b97479e399eae76e02817428dc9a37d0ca6e52588c84895dbdbbca7a23b5f2f876cd77cd9c731dfd7ec8faf5cfa64a3c1af8432aeed24cf99792a006415e6931755ee4b38817be6ae7f4b68de841fecd01c510463a0c0f6a2d6a1412638f121cfee907f4936d71cbadde975d8af59dcfda3d437c36587e6b0b7d42bb5f85849d0e9f07b8db19b2fd5893e3fd159b8ae34d58feecb6feb8c9f359e935c114461336c97f"
B = "10"
p = "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"
"""
      "p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "B": "0xb4dd14f591ec0dc4ec9540ad4a9dbd642cd9d0de4aaf9da90b9738dfdb88d11d24b1f0e5a923682a8517606aebd40cff9163c763874b480c47a4c544fe6196e3014aca72f52ec7aa4e98e3a111eed5c6e86eee4ebdafacd34e5de2ee087a39ac9593c997f35a2d9a9116e474202c6553d544f589afd1d504d79073fe092cbb45fed6ad9b2f593588a60b257b6640ca0dcee7bd396f4694094723d315865ffbbdff6c2c1b1f47c344ae1cd5a050ce144a7173adb020b88e8b41d56ac226182c1"}
      Intercepted from Alice: {"iv": "53c43184cce93f80b325b56ab10a3cee", 
      "encrypted_flag": "ba8f323668814d5403485c3dc83ae4229a558a873b507aa2cd956f07091164ff"}
"""
# thay đổi B trong cuộc trò chuyện của Bob và Alice
p = int(p,16)
A = int(A,16)
B = int(B,16)
for b in range(p):
      if pow(g,b,p) == B:
            print(b)
            break
print(pow(A,b,p))







